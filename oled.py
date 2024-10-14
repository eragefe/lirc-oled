from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from time import sleep
from datetime import datetime
from PIL import ImageFont
from alsaaudio import Mixer
import smbus
import time
import os.path
import subprocess

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
bus = smbus.SMBus(1)

while True:
	eth = os.popen('hostname -I').read().strip()
	vol = Mixer('Headphone').getvolume()
	vol = int(vol[0])
	#time = datetime.now().strftime("%H:%M")
	#date = datetime.now().strftime("%d/%m/%y")

	if vol < 100 and vol > 9:
		with canvas(device) as draw:
			FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",10)
			draw.text((25, 0), str(eth), font=FontTemp, fill="white")
			FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",50)
			draw.text((35, 15), str(vol), font=FontTemp, fill="white")
	elif vol == 100:
		with canvas(device) as draw:
			FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",10)
			draw.text((25, 0), str(eth), font=FontTemp, fill="white")
			FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",50)
			draw.text((35, 15), str("99"), font=FontTemp, fill="white")
	elif vol <10:
		with canvas(device) as draw:
			FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",10)
			draw.text((25, 0), str(eth), font=FontTemp, fill="white")
			FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",50)
			draw.text((45, 15), str(vol), font=FontTemp, fill="white")

sleep(0.5)
