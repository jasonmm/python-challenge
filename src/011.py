#!/usr/bin/python
"""
References:
http://www.pythonchallenge.com/pc/return/5808.html
http://unixwars.com/2007/09/17/python-challenge-level-11-odd-even/
"""

import argparse
import Image

parser = argparse.ArgumentParser(description="Python Challenge #011", add_help=True)
parser.add_argument("imagefile", metavar="imagefile", default="011.png", help="The image file to use.")
args = parser.parse_args()

im = Image.open(args.imagefile, 'r')
pix = im.load()
size = im.size

cur_pixel = 0

for x in range(size[0]):
    for y in range(size[1]):
        if (x+y)%2 != 0:
            # Note: we cannot use white pixels here (tried that) because the 
            # message does not stand out.
            pix[x,y] = (0,0,0)

im.save(args.imagefile+"-out.png", "PNG")

