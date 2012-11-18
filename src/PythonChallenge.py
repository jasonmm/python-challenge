import re

def next_nothing(data):
    return re.search("ext nothing is (\d{1,})", data)

