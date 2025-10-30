import time
import digitalio

class RotaryEncoder:
    """
    RotaryEncoder(pin_a, pin_b, *, pull=digitalio.Pull.UP, debounce_ms=3, pulses_per_detent=4)

    - pin_a, pin_b: board pin objects (e.g. board.D1, board.D0)
    - debounce_ms: stable time (ms) before accepting a new state 
    - pulses_per_detent: number of encoder edges per visible detent. Set to 1 if you want
      raw edges, or to 4 for many encoders so 1 detent == 1 step.
    """

    # Quadrature Table
    _TRANSITIONS = {
        0b0001:  1,  
        0b0011:  1,  
        0b0111:  1,  
        0b0100: -1,  
        0b1110:  1,  
        0b1101: -1,  
        0b1000:  1,  
        0b1011: -1,  
        }

    def __init__(self, pin_a, pin_b, *, pull=digitalio.Pull.UP, debounce_ms=3, pulses_per_detent=3):
        self._a = digitalio.DigitalInOut(pin_a)
        self._a.switch_to_input(pull=pull)
        self._b = digitalio.DigitalInOut(pin_b)
        self._b.switch_to_input(pull=pull)

        self._debounce_ms = max(1, int(debounce_ms))
        self._pulses_per_detent = max(1, int(pulses_per_detent))

        self._last_raw = (self._a.value, self._b.value)
        self._last_stable = self._last_raw
        self._last_change_time = time.monotonic() * 1000.0 

        self._last_q = (1 if self._last_stable[0] else 0) << 1 | (1 if self._last_stable[1] else 0)

        self._position_raw = 0
        self._position = 0
        self._delta_accum = 0

    @staticmethod
    def _pack(state):
        
        return (1 if state[0] else 0) << 1 | (1 if state[1] else 0)

    def _read_raw(self):
        return (self._a.value, self._b.value)

    def update(self):
        now = time.monotonic() * 1000.0
        raw = self._read_raw()
        if raw != self._last_raw:
            
            self._last_raw = raw
            self._last_change_time = now
            return False

        if raw != self._last_stable and (now - self._last_change_time) >= self._debounce_ms:
            prev_q = self._last_q
            self._last_stable = raw
            curr_q = self._pack(raw)
            self._last_q = curr_q

            key = (prev_q << 2) | curr_q
            move = self._TRANSITIONS.get(key, 0)

 
            if move == 0:
                diff = (curr_q - prev_q) % 4
                if diff == 1:
                    move = 1
                elif diff == 3:
                    move = -1
                elif diff == 2:
                    move = 2 if ( (curr_q - prev_q) > 0 ) else -2

            if move != 0:
                self._position_raw += int(move)

                new_pos = self._position_raw // self._pulses_per_detent
                if new_pos != self._position:
                    delta = new_pos - self._position
                    self._position = new_pos
                    self._delta_accum += delta
                    return True
        return False

    @property
    def position(self):
        return self._position

    @property
    def position_raw(self):
        return self._position_raw

    def get_delta(self):
        d = self._delta_accum
        self._delta_accum = 0
        return d

    def reset(self, *, to_detent=None):
        if to_detent is None:
            self._position_raw = 0
            self._position = 0
        else:
            self._position = int(to_detent)
            self._position_raw = self._position * self._pulses_per_detent
        self._delta_accum = 0

    
