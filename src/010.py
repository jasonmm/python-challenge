#!/usr/bin/python
"""
References:
http://www.pythonchallenge.com/pc/return/bull.html
http://unixwars.com/2007/09/16/python-challenge-level-10-where-are-you-looking-at/
"""


def a(prev_num):
    prev_digit = ''
    count = 0
    next_num = ''

    for index in range(len(prev_num)):
        if prev_num[index] != prev_digit:
            if count > 0:
                next_num += str(count)+prev_digit
                count = 0
            prev_digit = prev_num[index]
        count += 1

    next_num += str(count)+prev_digit

    return(next_num)
                


prev_num = "1"
a_list = []

print "a[0] = "+prev_num

for index in range(1,31):
    prev_num = a(prev_num)
    print "a["+str(index)+"] = "+prev_num
    a_list.append(prev_num)
    
print
print "a[30] has length of: "+str(len(a_list[29]))

