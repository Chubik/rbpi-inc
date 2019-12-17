import sys

import epd2in13b
from PIL import Image, ImageDraw, ImageFont

epd = epd2in13b.EPD() 
epd.init()           

def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in13b.EPD_WIDTH, epd2in13b.EPD_HEIGHT), 255)
    HRedImage = Image.new('1', (epd2in13b.EPD_WIDTH, epd2in13b.EPD_HEIGHT), 255)
    
    draw = ImageDraw.Draw(HBlackImage) 
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 30) 
    
    draw.text((5, 6), string, font = font, fill = 0)

    # epd2in13b.clear_frame_memory(0xFF)
    epd2in13b.set_frame_memory()
    epd2in13b.set_frame_memory(image.rotate(90), 0, 0)
    
    epd.display_frame(epd.get_frame_buffer(HBlackImage), epd.get_frame_buffer(HRedImage))
    
printToDisplay("Hello, World!")    