#!/usr/bin/python
"""
Counts the occurance of each character in the input text.

References:
http://www.pythonchallenge.com/pc/def/ocr.html (problem)
http://unixwars.com/2007/09/08/python-challenge-level-2-ocr/comment-page-1/#comment-350 (answer)
"""

import sys
import string

data = ""
for line in sys.stdin:
    data += line.strip()

for ch in string.punctuation:
    try:
        data = data.replace(ch, '')
    finally:
        pass

print data

# My original answer, but I like the above better.
#import operator
#
#counts = {}
#
#for line in sys.stdin:
#    line = line.strip()
#    for i in range(len(line)):
#        ch = line[i]
#        if ch in counts:
#            counts[ch] += 1
#        else:
#            counts[ch] = 1
#
#print sorted(counts.iteritems(), key=operator.itemgetter(1))


