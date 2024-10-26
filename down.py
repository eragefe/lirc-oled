import os
import smbus
bus = smbus.SMBus(1)

vol = bus.read_byte_data(0x48, 15)-1

bus.write_byte_data(0x48, 15, vol)
bus.write_byte_data(0x48, 16, vol)
