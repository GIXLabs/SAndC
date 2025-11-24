import time
import board
import pwmio
import digitalio
import supervisor

# ========= EDIT YOUR PINS HERE (avoid SPI pins used by LS7366) =========
PWM_PIN  = board.D6   # -> L298N ENA (remove ENA jumper)
DIR1_PIN = board.D2   # -> L298N IN1
DIR2_PIN = board.D3   # -> L298N IN2
# =======================================================================

PWM_FREQ_HZ  = 20000       # 20 kHz = quiet motor PWM
MAX_DUTY     = 65535
DEADTIME_S   = 0.050       # 50 ms coast when reversing
MIN_DUTY_PCT = 0           # static-friction floor if needed

# --- Initialize hardware ---
pwm = pwmio.PWMOut(PWM_PIN, frequency=PWM_FREQ_HZ, duty_cycle=0)
dir1 = digitalio.DigitalInOut(DIR1_PIN); dir1.direction = digitalio.Direction.OUTPUT
dir2 = digitalio.DigitalInOut(DIR2_PIN); dir2.direction = digitalio.Direction.OUTPUT

enabled   = True
direction = 1      # +1 or −1
duty_pct  = 50    # 0–100 %

def set_dir(sign: int):
    """Safe direction change: coast + deadtime, then set IN1/IN2."""
    global direction
    sign = 1 if sign >= 0 else -1
    if sign != direction:
        pwm.duty_cycle = 0
        dir1.value = dir2.value = False
        time.sleep(DEADTIME_S)
        direction = sign
    dir1.value, dir2.value = (True, False) if direction > 0 else (False, True)

def pct_to_duty(pct: float) -> int:
    pct = max(0.0, min(100.0, pct))
    if pct > 0 and pct < MIN_DUTY_PCT:
        pct = MIN_DUTY_PCT
    return int((pct / 100.0) * MAX_DUTY)

def set_duty_pct(pct: float):
    global duty_pct
    duty_pct = max(0.0, min(100.0, pct))
    pwm.duty_cycle = pct_to_duty(duty_pct) if enabled else 0

def set_enabled(en: bool):
    global enabled
    enabled = bool(en)
    pwm.duty_cycle = pct_to_duty(duty_pct) if enabled else 0

def set_pwm_freq(hz: int):
    current = pwm.duty_cycle
    pwm.frequency = max(100, int(hz))
    pwm.duty_cycle = current

def stop_motor():
    """Immediately stop the motor safely."""
    pwm.duty_cycle = 0
    dir1.value = dir2.value = False
    print("⚠ Motor stopped safely.")

def help_text():
    print(
        "\nCommands:\n"
        "  d <0-100>   : set PWM duty %\n"
        "  dir <1|-1>  : change direction (with deadtime)\n"
        "  f <Hz>      : change PWM frequency\n"
        "  start/stop  : enable or disable outputs\n"
        "  status      : print current state\n"
        "  help        : show this message\n"
        "Press Ctrl+C anytime → motor stops safely.\n"
    )

def print_status():
    print(f"enabled={enabled}  dir={direction}  duty={duty_pct:.1f}%  f={pwm.frequency} Hz")

# --- Startup ---
set_dir(direction)
set_enabled(True)
help_text()
print_status()

try:
    while True:
        if supervisor.runtime.serial_bytes_available:
            try:
                line = input().strip()
            except EOFError:
                line = ""
            if not line:
                continue

            parts = line.split()
            cmd = parts[0].lower()

            try:
                if cmd == "d" and len(parts) == 2:
                    set_duty_pct(float(parts[1])); print_status()
                elif cmd == "dir" and len(parts) == 2:
                    set_dir(int(parts[1])); print_status()
                elif cmd == "f" and len(parts) == 2:
                    set_pwm_freq(int(float(parts[1]))); print_status()
                elif cmd == "start":
                    set_enabled(True); print_status()
                elif cmd == "stop":
                    set_enabled(False); print_status()
                elif cmd == "status":
                    print_status()
                elif cmd == "help":
                    help_text()
                else:
                    print("Unknown command. Type 'help'.")
            except Exception as e:
                print("Error:", e)

        time.sleep(0.002)

except KeyboardInterrupt:
    # Safe stop on Ctrl + C
    stop_motor()
    print("Program interrupted by user (Ctrl + C). Exiting…")
