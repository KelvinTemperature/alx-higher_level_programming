#!/usr/bin/python3
lcase = ord('z')
ucase = ord('Y')

while (lcase >= ord('a') and ucase >= ord('A')):
    print(chr(lcase) + chr(ucase), end='')
    lcase -= 2
    ucase -= 2
print()
