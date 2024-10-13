from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
from time import sleep
from datetime import datetime
from PIL import ImageFont
import smbus
import time
from alsaaudio import Mixer

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
bus = smbus.SMBus(1)

while True:

        vol = Mixer('Headphone').getvolume()
        vol2 = int(vol[0])
        #time = datetime.now().strftime("%H:%M")
        #date = datetime.now().strftime("%d/%m/%y")

        if vol2 < 100 and vol2 > 9:
                with canvas(device) as draw:
                        FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",60)
                        draw.text((30, 0), str(vol2), font=FontTemp, fill="white")
        elif vol2 == 100:
                with canvas(device) as draw:
                        FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",40)
                        draw.text((30, 0), str("max"), font=FontTemp, fill="white")
        elif vol2 <10:
                with canvas(device) as draw:
                        FontTemp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",60)
                        draw.text((50, 0), str(vol2), font=FontTemp, fill="white")
sleep(1)
