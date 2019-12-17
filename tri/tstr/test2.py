import time
import logging
import epd2in13b

from PIL import Image, ImageDraw, ImageFont

epd = epd2in13b.EPD()
epd.init()

h = 200;  w = 200 # e-paper heigth and width.

buf_black        = bytearray(w * h // 8) # used by frame buffer (landscape)
buf_red          = bytearray(w * h // 8) # used by frame buffer (landscape)
buf_epaper_black = bytearray(w * h // 8) # used to display on e-paper after bytes have been
buf_epaper_red   = bytearray(w * h // 8) # moved from frame buffer to match e-paper (portrait)

import framebuf
fb_black = framebuf.FrameBuffer(buf_black, w, h, framebuf.MONO_VLSB)
fb_red   = framebuf.FrameBuffer(buf_red,   w, h, framebuf.MONO_VLSB)
black_red = 0 # will be black on buf_black, red on buf_red
white     = 1

#clear red & black screens, write in black on top left and in red bootom right
fb_black.fill(white)
fb_red.fill(white)
fb_black.text('Hello world!', 0, 0,black_red)
fb_red.text('Hello world!', 110, 90,black_red)

# Move frame buffer bytes to e-paper buffer to match e-paper bytes oranisation.
# That is landscape mode to portrait mode. (for red and black buffers)
for i in range(0, 25):
    for j in range(0, 200):
        m = (n-x)+(n-y)*24
        buf_epaper_black[m] = buf_black[n]
        buf_epaper_red[m] = buf_red[n]
        n +=1
    x = n+i+1
    y = n-1

print('Sending to display')
epd.display_frame(buf_epaper_black, buf_epaper_red)
print('Done!.......')