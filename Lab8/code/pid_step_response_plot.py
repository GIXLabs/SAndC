# Captures three full cycles (each = 8 s: 2 rps for 4 s, then 3 rps for 4 s)
# Plots commanded vs actual velocity for the captured window.

import sys, serial, matplotlib.pyplot as plt

# ===== USER SETUP =====
serialPort = None
usingPorts = list(list_ports.comports())
for port in usingPorts:
    #debug to detect Serial name
    print(port.description)
    if sys.platform.startswith('win'):
        if "Serial" in port.description:
            serialPort = port.device
            break
        # end
    elif sys.platform.startswith('darwin'):
        if "Sense" in port.description:
            serialPort = port.device
            break
SERIAL_PORT = serialPort   # you might need to change this manually if auto detection does not work
BAUD = 115200
TIMEOUT_S = 0.5
# ======================

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD, timeout=TIMEOUT_S)
    except Exception as e:
        print("Failed to open serial port:", e); sys.exit(1)

    times, cmds, acts = [], [], []
    started = False
    cycles_seen = 0

    print("Listening… Capturing 3 cycles (watch for CYCLE_START/END).")

    try:
        while True:
            line = ser.readline()
            if not line: continue
            try:
                s = line.decode("utf-8", errors="replace").strip()
            except Exception:
                continue
            if not s: continue

            if s.startswith("CYCLE_START"):
                if not started:
                    started = True
                continue

            if s.startswith("CYCLE_END"):
                cycles_seen += 1
                if cycles_seen >= 3:
                    print("Got 3 cycles. Plotting…")
                    break
                continue

            # DATA,t,cycle,cmd_rps,act_rps
            if started and s.startswith("DATA,"):
                parts = s.split(",")
                if len(parts) == 5 and parts[1] != "t":
                    try:
                        t = float(parts[1]); cmd = float(parts[3]); act = float(parts[4])
                    except ValueError:
                        continue
                    times.append(t); cmds.append(cmd); acts.append(act)
    finally:
        try: ser.close()
        except Exception: pass

    if not times:
        print("No data captured. Is the board streaming DATA lines?")
        sys.exit(1)

    t0 = times[0]
    t_rel = [ti - t0 for ti in times]

    plt.figure()
    plt.plot(t_rel, cmds, label="Commanded velocity (rps)")
    plt.plot(t_rel, acts, label="Actual velocity (rps)")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (rps)")
    plt.title("Velocity Step Response: 2 rps ↔ 3 rps (3 cycles)")
    plt.grid(True); plt.legend(); plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
