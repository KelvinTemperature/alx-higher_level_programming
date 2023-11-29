#!/usr/bin/python3
lcase = 'z'
ucase = 'Y'

while (ord(lcase) >= ord('a') and ord(ucase) >= ord('A')):
    print("{}{}".format(lcase, ucase), end='')
    lcase = chr(ord(lcase) - 2)
    ucase = chr(ord(ucase) - 2)
print()
