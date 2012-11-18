#!/usr/bin/python
"""

References:
http://www.pythonchallenge.com/pc/def/linkedlist.php
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
"""

import urllib
import PythonChallenge

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#nothings = [12345]
nothings = [8022]

def get_url_contents(nothing):
    print base_url+str(nothing)
    return urllib.urlopen(base_url+str(nothing)).read()


for i in range(400):
    contents = get_url_contents(nothings[-1:].pop())
    next_nothing = PythonChallenge.next_nothing(contents)
    if next_nothing == None:
        print contents
        break;
    nothings.append(next_nothing.groups()[0])

print nothings    

