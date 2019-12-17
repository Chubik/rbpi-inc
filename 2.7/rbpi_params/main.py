# coding=utf-8

import sys
sys.path.insert(1, '../drivers/')


import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import epd2in7
import psutil


W = epd2in7.EPD_WIDTH
H = epd2in7.EPD_HEIGHT
size = (W, H)

epd = epd2in7.EPD()
epd.init()

def collect_meminfo():
        meminfo = psutil.virtual_memory()
        memdict = {}
        memdict['total'] = meminfo.total/1024
        memdict['used'] = meminfo.used/1024
        memdict['free'] = meminfo.free/1024
        memdict['buffers'] = meminfo.buffers/1024
        memdict['cached'] = meminfo.cached/1024
        memdict['percent'] = meminfo.percent
        return memdict

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=", "").replace("'C\n", ""))


mask = Image.new('1', (H,W), 255)    # 255: clear the image with white; H,W for rotation
draw = ImageDraw.Draw(mask)
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 14)
temp = float(getCPUtemperature())

line = 1
draw.text((1,line), 'CPU temperature: ' + str(temp), font=font, fill=0)

mm = collect_meminfo()

line = line + 20
draw.text((1,line), "MEMORY --", font=font, fill=0)


for key, value in mm.items():
    line = line + 20
    draw.text((1,line), str(key)+': ' + str(value), font=font, fill=0)


mask = mask.rotate(90, expand=True)
epd.display_frame(epd.get_frame_buffer(mask))
