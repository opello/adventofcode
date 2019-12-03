#!/usr/bin/env python

total = 0

with open('../inputs/01.txt') as f:
    for i, line in enumerate(f):
        mass = int(line)
        fuel = (mass / 3) - 2
        total += fuel
        #print('>>> mass={0} fuel={1}'.format(mass, fuel))

print total
