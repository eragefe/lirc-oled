from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from time import sleep
from PIL import ImageFont
import smbus
import os.path
import subprocess

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
bus = smbus.SMBus(1)

eth = os.popen('hostname -I').read().strip()

while True:
          f = open("/root/vol", "r")
          vol= int(f.read())
          if vol < 100 and vol > 9:
               with canvas(device) as draw:
                    FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",10)
                    draw.text((25, 0), str(eth), font=FontTemp, fill="white")
                    draw.text((100, 40), ("db"), font=FontTemp, fill="white")
                    FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",50)
                    draw.text((35, 13), str(vol), font=FontTemp, fill="white")
                    draw.text((5, 15), ("-"), font=FontTemp, fill="white")
          elif vol >= 100:
               with canvas(device) as draw:
                    FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",10)
                    draw.text((25, 0), str(eth), font=FontTemp, fill="white")
                    draw.text((100, 40), ("db"), font=FontTemp, fill="white")
                    FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",50)
                    draw.text((35, 13), str(99), font=FontTemp, fill="white")
                    draw.text((5, 15), ("-"), font=FontTemp, fill="white")
          elif vol < 10 and vol > 0:
               with canvas(device) as draw:
                    FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",10)
                    draw.text((25, 0), str(eth), font=FontTemp, fill="white")
                    draw.text((100, 40), ("db"), font=FontTemp, fill="white")
                    FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",50)
                    draw.text((47, 13), str(vol), font=FontTemp, fill="white")
                    draw.text((5, 15), ("-"), font=FontTemp, fill="white")
          elif vol <= 0:
               with canvas(device) as draw:
                    FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",10)
                    draw.text((25, 0), str(eth), font=FontTemp, fill="white")
                    draw.text((100, 40), ("db"), font=FontTemp, fill="white")
                    FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",50)
                    draw.text((47, 13), str(0), font=FontTemp, fill="white")
                    draw.text((5, 15), ("-"), font=FontTemp, fill="white")
sleep(0.1)
