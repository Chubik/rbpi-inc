import sys
sys.path.insert(1, '../drivers/')


import epd2in7

from PIL import Image
im = Image.open('main.png')
im.show()
