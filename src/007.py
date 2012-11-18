#!/usr/bin/python
"""

References:
http://www.pythonchallenge.com/pc/def/oxygen.html
http://unixwars.com/2007/09/13/python-challenge-level-7-smarty/
"""

import argparse
import Image

parser = argparse.ArgumentParser(description="Python Challenge #007", add_help=True)
parser.add_argument("imagefile", metavar="imagefile", default="007.png", help="The image file to use.")
args = parser.parse_args()

im = Image.open(args.imagefile, 'r')
pix = im.load()
size = im.size

answer = ""
# We know each grey area is exactly 7 pixels wide
for x in range(0, size[0], 7):
	# We know that y=50 will always be on the grey line
	val = pix[x, 50][0]
	answer += chr(val)
print answer


answer = ""
next_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
for i in next_list:
	answer += chr(i)
print answer
