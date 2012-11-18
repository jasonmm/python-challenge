#!/usr/bin/python
"""
References:
http://www.pythonchallenge.com/pc/return/italy.html
http://unixwars.com/2007/09/20/python-challenge-level-14-walk-around/

The hints given were particularly obtuse.  The sequence (100*100) = ...
was especially misleading.  Taher's solution using vectors is definitely
the way to go once you realize what is needed.
"""

import Image
import ImageDraw


def next_direction(cur):
    if cur+1 >= directions.length:
        return 0
    return cur+1

def get_next_pixel(cur_pixel, cur_direction):
    next_pixel[0] = cur_pixel[0] + cur_direction[0]
    next_pixel[1] = cur_pixel[1] + cur_direction[1]
    return next_pixel


im = Image.open("../data/014.png")
im_out = Image.new("P", (100,100), 0)
im_out_d = ImageDraw.Draw(im_out)

directions = [ (1,0), (0,1), (-1,0), (0,-1) ]
cur_direction = 0
cur_pixel = (0,0)
next_pixel = (0,0)

pix = im.load()

for p in range(im.size[0]):
    # Place the pixel
    im_out_d.point(cur_pixel, pix[p,0])
    # Determine the next pixel in the current direction
    get_next_pixel(cur_pixel, directions[cur_direction])
    # Check to see if we have moved outside the image
    if next_pixel[0] > im_out.size[0] or next_pixel[1] > im_out.size[1]:
        # We are outside the image so we change direction and 
        # re-calculate our next pixel
        cur_direction = next_direction(cur_direction)
        next_pixel = get_next_pixel(cur_pixel, directions[cur_direction])
    # Check to see if we have encountered a non-black pixel.  We keep changing
    # direction until we find one where the next pixel in that direction is
    # not black.
    failed_color_checks = 0
    while im_out.getpixel((next_pixel[0], next_pixel[1])) != (0,0,0):
        if failed_color_checks > directions.length:
            break;
        cur_direction = next_direction(cur_direction)
        next_pixel = get_next_pixel(cur_pixel, directions[cur_direction])

    # There no black pixels surrounding our current pixel so we are done.
    if failed_color_checks > directions.length:
        break;
    
    # Move to the next pixel.
    cur_pixel = next_pixel

#for y in range(100):
#    for x in range(100):
#        x1 = x
#        if y%2 != 0:
#            x1 = 100-x
#        im_out_d.point((x1,y), fill=pix[x+y, 0])

im_out.save("../data/014-out.png", "PNG")

