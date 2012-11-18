#!/usr/bin/python
"""

References:
http://www.pythonchallenge.com/pc/def/channel.html
http://www.pythonchallenge.com/pc/def/channel.zip
http://unixwars.com/2007/09/12/python-challenge-level-6-now-there-are-pairs/ (answer)
"""

import argparse
import zipfile
import PythonChallenge

parser = argparse.ArgumentParser(description="Python Challenge #006", add_help=True)
parser.add_argument("zipfile", metavar="zipfile", default="006.zip", help="The zip file to use.")
args = parser.parse_args()

nothing = "90052"
comments = ""

try:
    if zipfile.is_zipfile(args.zipfile) == False:
        raise zipfile.BadZipfile 
    z = zipfile.ZipFile(args.zipfile)
    while True:
        # The name of the next file to process
        name = nothing+".txt"

        # Append the file's comment
        comments += z.getinfo(name).comment

        # Open the file to get the next file to process
        nothing_file = z.open(name)
        contents = nothing_file.read()
        next_nothing = PythonChallenge.next_nothing(contents)
        if next_nothing == None:
            print contents
            break;
        nothing = next_nothing.groups()[0]

    print comments

except zipfile.BadZipfile:
    print args.zipfile+" is not a valid ZIP file."
finally:
    if z:
        z.close()

