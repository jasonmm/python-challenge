#!/usr/bin/python
"""
Finds occurances of one lowercase that has exactly three uppercase letters
on either side of it.

References:
http://www.pythonchallenge.com/pc/def/equality.html (problem)
http://unixwars.com/2007/09/09/python-challenge-level-3-re/ (answer)
"""

import sys
import re

data = ""
for line in sys.stdin:
    data += line.strip()

print "".join(re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", data))

# My original answer prior to discovering the findall method.
#matches = re.finditer("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", data)
#
#word = ""
#try:
#    m = matches.next()
#    while True:
#        word += m.groups()[0]
#        m = matches.next()
#except StopIteration:
#    pass
#
#print word
