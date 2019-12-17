import os
import sys
sys.path.insert(1, '../drivers/')


file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import epd2in7

from PIL import Image, ImageDraw, ImageFont

def main():
        #Init driver
        epd = epd2in7.EPD()
        epd.init()

        #Image de la dimension de l ecran - Image with screen size
        #255: fond blanc - clear the image with white
        image = Image.new('1', (epd2in7.EPD_WIDTH, epd2in7.EPD_HEIGHT), 255)    
        #Objet image sur lequel on va dessiner - Object image on which we will draw
        draw = ImageDraw.Draw(image)

        #Dessine un rectangle au centre de l ecran - draw a rectangle in the center of the screen
        draw.rectangle((epd2in7.EPD_WIDTH/2-10, epd2in7.EPD_HEIGHT/2-10, epd2in7.EPD_WIDTH/2+10, epd2in7.EPD_HEIGHT/2+10), fill = 0)

        #Actualise affichage - Update display
        epd.display_frame(epd.get_frame_buffer(image))

if __name__ == '__main__':
    main()