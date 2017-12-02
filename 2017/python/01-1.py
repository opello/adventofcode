#!/usr/bin/env python

total = 0
firstdigit = 0
digit = 0

with open('../inputs/01.txt') as f:
    digit = int(f.read(1))
    firstdigit = digit
    while True:
        tmp = f.read(1)
        try:
            tmp = int(tmp)
        except:
            if digit == firstdigit:
                total += firstdigit
            break
        if tmp == digit:
            total += tmp
        else:
            digit = tmp

print total
