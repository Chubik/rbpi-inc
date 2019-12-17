import time
import logging
import epd2in13b

from PIL import Image, ImageDraw, ImageFont

epd = epd2in13b.EPD()
epd.init()
EPD_WIDTH = epd2in13b.EPD_WIDTH  # 104 pixels
EPD_HEIGHT = epd2in13b.EPD_HEIGHT  # 212 pixels


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


def printMaskToEinkScreen(string):

    HBlackImage = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
    HRedImage = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)

    draw = ImageDraw.Draw(HRedImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    
    draw.text((10, 65), string, font = normalfont, fill = 0)

    rotateRedMask = HRedImage.rotate(0)
    rotateBlackMask = HBlackImage.rotate(0)
    epd.display_frame(epd.get_frame_buffer(rotateBlackMask),epd.get_frame_buffer(rotateRedMask))
    # epd.display_frame(epd.get_frame_buffer(rotatedMask))
    # epd.display_frame(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))
def logError(e):
    logging.error("{} ({}): {}".format(e.__class__, e.__doc__, e.message))


if __name__ == '__main__':
    running = True
    while running:
        try:
            lastUpdated = time.strftime('%a %d.%m %H:%M')
            printMaskToEinkScreen(lastUpdated)
        except Exception as e:
            logError (e)
            print(e)
        time.sleep(600)
        # Refreshes every 10 minutes


# printMaskToEinkScreen("Hello")