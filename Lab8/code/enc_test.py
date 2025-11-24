import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_bus_device.spi_device import SPIDevice

# SPI setup (modify pins if needed)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = DigitalInOut(board.D1)
cs.direction = Direction.OUTPUT

device = SPIDevice(spi, cs, baudrate=1000000, polarity=0, phase=0)

# LS7366 Commands
CLEAR_CNTR = 0x20  # clear counter
CLEAR_STR  = 0x30  # clear status
READ_CNTR  = 0x60  # read counter
WRITE_MDR0 = 0x88  # write mode register 0
WRITE_MDR1 = 0x90  # write mode register 1

# MDR0 bits: x4 quadrature, free-running, no index
MDR0_CONFIG = 0b00000011
# MDR1 bits: 4-byte counter mode
MDR1_CONFIG = 0b00000000

def ls7366_write(cmd, data=None):
    """Send command + optional data bytes."""
    if data is None:
        data = []
    with device as spi_dev:
        spi_dev.write(bytes([cmd] + data))

def ls7366_read(cmd, nbytes):
    """Read nbytes from LS7366."""
    with device as spi_dev:
        buf = bytearray([cmd] + [0x00]*nbytes)
        spi_dev.write_readinto(buf, buf)
        return buf[1:]  # skip first byte (command)

# Initialize LS7366
time.sleep(0.1)
ls7366_write(WRITE_MDR0, [MDR0_CONFIG])
ls7366_write(WRITE_MDR1, [MDR1_CONFIG])
ls7366_write(CLEAR_CNTR)
ls7366_write(CLEAR_STR)

print("LS7366 initialized. Reading encoder...")

while True:
    data = ls7366_read(READ_CNTR, 4)
    # count = int.from_bytes(data, 'big', signed=False)
    raw = int.from_bytes(data, 'big', signed=False)
    count = raw - (1 << 32) if (raw & (1 << 31)) else raw
    print("Count:", count)
    time.sleep(0.1)
