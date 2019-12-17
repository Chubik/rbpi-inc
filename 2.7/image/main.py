import sys
sys.path.insert(1, '../drivers/')


import epd2in7
from resizeimage import resizeimage

from PIL import Image
W = epd2in7.EPD_WIDTH
H = epd2in7.EPD_HEIGHT
size = (W,H)

epd = epd2in7.EPD()
epd.init()


img = Image.new('L', size, 255)
img = Image.open('main.png','r')

width, height = img.size[:2]

# make a white background for image
background = Image.new('RGBA', size, (255, 255, 255, 255))

# resize image
if height > width:
    hpercent = (H/float(img.size[1]))
    wsize = int((float(img.size[0])*float(hpercent)))
    img = img.resize((wsize, H), Image.ANTIALIAS)
else:
    wpercent = (W/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((W,hsize), Image.ANTIALIAS)

# paste image on background
background.paste(img, (0,0))
epd.display_frame(epd.get_frame_buffer(background))
