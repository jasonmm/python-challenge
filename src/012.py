#!/usr/bin/python
"""
References:
http://www.pythonchallenge.com/pc/return/evil.html

Solution:
  The two solutions below both use "i" to iterate over the five
interleaved images.  The [i::5] tells the program to start at number i
and go to the end of "info" using step 5.  Thus [i::5] gets a sequence of
bytes using every 5th byte from "info" between "i" and the end of "info".

So for the first interleaved image "i" will be 0.  So the sequence that [i::5]
returns will the bytes at 0,5,10,15,etc...  And for the second interleaved
image "i" will be 1 so the sequence of bytes will be 1,6,11,16,etc...

Slicing notation is apparently quite powerful and versatile. :)
"""


gfxfile = "../data/evil2.gfx"

"""
solution stolen from: http://unixwars.com/2007/09/18/python-challenge-level-12-dealing-evil/
"""
info=open(gfxfile).read()
[open("12_f%d.dat" %i, "w").write(info[i::5]) for i in range(5)]

"""
solution stolen from: http://garethrees.org/2007/05/07/python-challenge/
"""
types = ['jpg','png','gif','png','jpg']
for i in range(5): 
    open('evil2%d.%s' % (i, types[i]),'wb').write(info[i::5])
