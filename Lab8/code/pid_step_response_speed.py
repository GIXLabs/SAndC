# Continuous velocity step response: 2 rps (4 s) -> 3 rps (4 s) -> repeat
# Streams: DATA,t,cycle,cmd_rps,act_rps
# Markers: CYCLE_START,<n>, CYCLE_END,<n>
# Board: XIAO ESP32S3  |  Motor: L298N ENA=D6, IN1=D2, IN2=D3  |  Encoder: LS7366 CS=D1

import time, board, pwmio, digitalio, busio
from adafruit_bus_device.spi_device import SPIDevice
import time

time.sleep(3) 
# =================== USER SETTINGS ===================
CPR                 = 3000
LOW_RPS             = 2.0          # 2 rounds/second
HIGH_RPS            = 3.0          # 3 rounds/second
SEGMENT_S           = 4.0          # each segment duration
CYCLE_S             = 2 * SEGMENT_S

# Velocity loop gains (duty_fraction per rps of error)
VKP = 3
VKI = 0.50
VKD = 0.00

# Control loop / PWM
LOOP_DT_S           = 0.005        # ~200 Hz
PWM_FREQ_HZ         = 20000
DEADTIME_S          = 0.030

# Heavy-friction helpers
BREAKAWAY_DUTY_PCT  = 65.0         # used only until motion established
MIN_DUTY_MOVE_PCT   = 10.0         # minimum while moving

# Velocity estimation
VEL_LP_ALPHA        = 0.25         # 0..1; higher = snappier estimate
VEL_DEADBAND_RPS    = 0.03

# Pins
PWM_PIN  = board.D6
DIR1_PIN = board.D2
DIR2_PIN = board.D3
CS_PIN   = board.D4
# =====================================================

# ---------------- Motor helpers ----------------
MAX_DUTY = 65535
pwm = pwmio.PWMOut(PWM_PIN, frequency=PWM_FREQ_HZ, duty_cycle=0)
dir1 = digitalio.DigitalInOut(DIR1_PIN); dir1.direction = digitalio.Direction.OUTPUT
dir2 = digitalio.DigitalInOut(DIR2_PIN); dir2.direction = digitalio.Direction.OUTPUT

def _pct_to_duty(p): return int((max(0.0, min(100.0, p)) / 100.0) * MAX_DUTY)
def _set_forward(): dir1.value, dir2.value = True, False
def _coast(): pwm.duty_cycle = 0; dir1.value = dir2.value = False
def _brake(pct=100.0):  # fast-brake (no reverse)
    dir1.value = True; dir2.value = True
    pwm.duty_cycle = _pct_to_duty(pct)

def _apply_output(u_frac, moving):
    """
    u_frac in [-1,+1]. Positive -> forward PWM, Negative -> active brake.
    Staged minimums for strong friction; no direction reversal used.
    """
    if u_frac >= 0.0:
        mag = u_frac
        duty_pct = 100.0 * mag
        if moving:
            if 0.0 < duty_pct < MIN_DUTY_MOVE_PCT: duty_pct = MIN_DUTY_MOVE_PCT
        else:
            if 0.0 < duty_pct < BREAKAWAY_DUTY_PCT: duty_pct = BREAKAWAY_DUTY_PCT

        # ensure forward direction
        # if previously braked or coasted, no need for deadtime
        _set_forward()
        pwm.duty_cycle = _pct_to_duty(duty_pct)

    else:
        # decelerate using fast-brake proportionally to demand
        mag = min(1.0, -u_frac)
        _brake(100.0 * mag)

def stop_motor(): _coast()

# ---------------- Encoder (LS7366) ----------------
CLEAR_CNTR = 0x20; CLEAR_STR = 0x30; READ_CNTR = 0x60
WRITE_MDR0 = 0x88; WRITE_MDR1 = 0x90
MDR0_CONFIG = 0b00000011   # x4 quadrature, free-run
MDR1_CONFIG = 0b00000000   # 4-byte counter

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs  = digitalio.DigitalInOut(CS_PIN); cs.direction = digitalio.Direction.OUTPUT
device = SPIDevice(spi, cs, baudrate=1_000_000, polarity=0, phase=0)

def _ls7366_write(cmd, data=None):
    if data is None: data=[]
    with device as sd: sd.write(bytes([cmd]+data))

def _ls7366_read(cmd, nbytes):
    with device as sd:
        buf = bytearray([cmd]+[0x00]*nbytes)
        sd.write_readinto(buf, buf)
        return buf[1:]

def enc_init():
    time.sleep(0.1)
    _ls7366_write(WRITE_MDR0, [MDR0_CONFIG])
    _ls7366_write(WRITE_MDR1, [MDR1_CONFIG])
    _ls7366_write(CLEAR_CNTR); _ls7366_write(CLEAR_STR)

def enc_clear(): _ls7366_write(CLEAR_CNTR)
def enc_read_count():
    d = _ls7366_read(READ_CNTR,4)
    raw = int.from_bytes(d,'big',signed=False)
    return raw - (1<<32) if (raw & (1<<31)) else raw

# ---------------- Velocity PID ----------------
class VelPID:
    def __init__(self, kp, ki, kd, umin=-1.0, umax=+1.0, i_clamp=0.8):
        self.kp=float(kp); self.ki=float(ki); self.kd=float(kd)
        self.umin=float(umin); self.umax=float(umax)
        self.i=0.0; self.i_clamp=float(i_clamp); self.e_prev=0.0
    def reset(self): self.i=0.0; self.e_prev=0.0
    def step(self, e, dt):
        d = (e - self.e_prev)/dt if dt>0 else 0.0
        u_unsat = self.kp*e + self.ki*self.i + self.kd*d
        u = max(self.umin, min(self.umax, u_unsat))
        # anti-windup
        if (u == u_unsat) or (u>0 and e<0) or (u<0 and e>0):
            self.i = max(-self.i_clamp, min(self.i_clamp, self.i + e*dt))
        self.e_prev = e
        return u

# ---------------- Main ----------------
print("VEL_STEP_CONTINUOUS, start")
print("DATA,t,cycle,cmd_rps,act_rps")

enc_init()
t0 = time.monotonic()
cycle = 0

try:
    # initial clear and gentle spin-up target = LOW_RPS
    enc_clear(); time.sleep(0.01)
    pid = VelPID(VKP, VKI, VKD)
    last_t   = time.monotonic()
    last_cnt = enc_read_count()
    vel_rps  = 0.0
    moving   = False
    cycle_t0 = time.monotonic()
    cycle = 1
    print(f"CYCLE_START,{cycle}")

    while True:
        now = time.monotonic()
        dt = now - last_t
        if dt <= 0: continue
        last_t = now
        t = now - t0

        # Which segment inside an 8s cycle?
        tau = now - cycle_t0
        if tau < SEGMENT_S:
            v_sp = LOW_RPS
        elif tau < CYCLE_S:
            v_sp = HIGH_RPS
        else:
            print(f"CYCLE_END,{cycle}")
            cycle += 1
            print(f"CYCLE_START,{cycle}")
            cycle_t0 = now
            v_sp = LOW_RPS  # new cycle begins at low
            # fall through to apply control this tick

        # Measured velocity
        cnt = enc_read_count()
        inst_vel = ((cnt - last_cnt) / CPR) / dt
        last_cnt = cnt
        vel_rps = (1.0 - VEL_LP_ALPHA)*vel_rps + VEL_LP_ALPHA*inst_vel
        if abs(vel_rps) < VEL_DEADBAND_RPS: vel_rps = 0.0

        # Velocity PID
        e = v_sp - vel_rps
        u = pid.step(e, dt)

        # Mark "moving" once actual vel exceeds threshold
        moving = moving or (abs(vel_rps) > 0.05)

        # Apply output: forward PWM or braking (no reverse)
        _apply_output(u, moving)

        # Stream
        print(f"DATA,{t:.4f},{cycle},{v_sp:.3f},{vel_rps:.3f}")

        # pace
        time.sleep(max(0.0, LOOP_DT_S - (time.monotonic() - now)))

except KeyboardInterrupt:
    stop_motor()
    print("INTERRUPTED")
