#!/usr/bin/python
"""

References:
http://www.pythonchallenge.com/pc/def/integrity.html
http://unixwars.com/2007/09/14/python-challenge-level-8-working-hard/
http://ubuntuforums.org/archive/index.php/t-664382.html (using the command-line)
"""

import argparse
import bz2

parser = argparse.ArgumentParser(description="Python Challenge #008", add_help=True)
parser.add_argument("datafile", metavar="datafile", default="008.txt", help="The data file to use.")
args = parser.parse_args()

username = ""
password = ""

for line in open(args.datafile):
	line = line.strip()
	parts = line.partition(':')
	if parts[0].strip() == "un":
		username = parts[2].strip("' ")
	elif parts[0].strip() == "pw":
		password = parts[2].strip("' ")


# Reading from the file does not work.  So we use the hard-coded method.
username = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084';
password = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08';

print bz2.decompress(username)
print bz2.decompress(password)


