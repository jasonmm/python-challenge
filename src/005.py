#!/usr/bin/python
"""

References:
http://www.pythonchallenge.com/pc/def/peak.html
http://unixwars.com/2007/09/11/python-challenge-level-5-peak-hell/
"""

import sys
import cPickle


data = sys.stdin.read().strip();

data = cPickle.loads(data)

print data

for item in data[:]:
    for i in item[:]:
        sys.stdout.write( i[0] * i[1] )
    print
