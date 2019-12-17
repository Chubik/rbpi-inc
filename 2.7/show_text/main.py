import sys
sys.path.insert(1, '../drivers/')


import time
import epd2in7

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

epd = epd2in7.EPD()
epd.init()
EPD_WIDTH = epd2in7.EPD_WIDTH  # 176 pixels
EPD_HEIGHT = epd2in7.EPD_HEIGHT  # 264 pixels

 
teenytinyfont = ImageFont.truetype(
    '/usr/share/fonts/truetype/freefont/FreeSans.ttf', 10)
teenyfont = ImageFont.truetype(
    '/usr/share/fonts/truetype/freefont/FreeSans.ttf', 12)
tinyfont = ImageFont.truetype(
    '/usr/share/fonts/truetype/freefont/FreeSans.ttf', 14)
smallfont = ImageFont.truetype(
    '/usr/share/fonts/truetype/freefont/FreeSans.ttf', 18)
normalfont = ImageFont.truetype(
    '/usr/share/fonts/truetype/freefont/FreeSans.ttf', 22)
medfont = ImageFont.truetype(
    '/usr/share/fonts/truetype/freefont/FreeSans.ttf', 40)
bigfont = ImageFont.truetype(
    '/usr/share/fonts/truetype/freefont/FreeSans.ttf', 70)


def printMaskToEinkScreen():
    lastUpdated = time.strftime('%a %d.%m %H:%M')

    global mask
    mask = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    # 255: clear the image with white
    draw = ImageDraw.Draw(mask)
    draw.text((98, 75), 'BELOW ZERO', font=teenyfont, fill=0)

    rotatedMask = mask.rotate(0)
    # Turns mask upside down, this just happened to work best for my frame
    # with regards to which side the cable came out.
    epd.display_frame(epd.get_frame_buffer(rotatedMask))
    print('Weather display successfully refreshed at {}'.format(time.strftime('%d%m%y-%H:%M:%S')))

printMaskToEinkScreen()