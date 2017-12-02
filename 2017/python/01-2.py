#!/usr/bin/env python

total = 0
numbers = []

with open('../inputs/01.txt') as f:
    while True:
        tmp = f.read(1)
        try:
            tmp = int(tmp)
            numbers += [tmp]
        except:
            break

for position, value in enumerate(numbers):
    nextPosition = (position + (len(numbers) / 2)) % len(numbers)
    if value == numbers[nextPosition]:
        total += value

print total
