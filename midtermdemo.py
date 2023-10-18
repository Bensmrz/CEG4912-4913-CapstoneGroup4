import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging    
import time
import traceback
from waveshare_OLED import OLED_1in51
from PIL import Image, ImageDraw, ImageFont
logging.basicConfig(level=logging.DEBUG)

try:
    disp = OLED_1in51.OLED_1in51()

    logging.info("\r1.51inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()

    while True:
        user_input = input("Enter text to display on the OLED (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break  # Exit the loop and quit the program

        # Create blank image for drawing.
        image1 = Image.new('1', (disp.width, disp.height), "WHITE")
        draw = ImageDraw.Draw(image1)
        font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
        font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

        # Clear the display.
        disp.clear()

        # Draw text on the OLED screen.
        draw.text((20, 0), user_input, font=font1, fill=0)

        # Rotate and display the image.
        image1 = image1.rotate(180)
        disp.ShowImage(disp.getbuffer(image1))
        time.sleep(3)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    OLED_1in51.config.module_exit()
    exit()
