#!/usr/bin/python
"""
References:
http://www.pythonchallenge.com/pc/return/disproportional.html
http://www.pythonchallenge.com/pc/phonebook.php
http://unixwars.com/2007/09/19/python-challenge-level-13-call-him/
"""

import xmlrpclib

URL = "http://www.pythonchallenge.com/pc/phonebook.php"

rpc = xmlrpclib.Server(URL);

allpages = rpc.system.listMethods()
print ", ".join(allpages)

allpages = rpc.phone("Bert")
print ", ".join(allpages)

# It appears that anything not "Bert" just returns
# "He is not the evil"
#allpages = rpc.phone("555-ITALY")
#print ", ".join(allpages)
#
#allpages = rpc.phone("Ernie")
#print ", ".join(allpages)
