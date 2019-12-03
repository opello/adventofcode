#!/usr/bin/env python

total = 0

def getFuel(mass):
    fuel = 0
    tmp = (mass / 3) - 2
    if tmp > 0:
        fuel = tmp
    
    return fuel

with open('../inputs/01.txt') as f:
    for i, line in enumerate(f):
        mass = int(line)
        fuel = getFuel(mass)
        total += fuel
        #print('>>> mass={0} fuel={1}'.format(mass, fuel))
        tmp = getFuel(fuel)
        while tmp > 0:
            #print('... fuel={0} tmp={1}'.format(fuel, tmp))
            total += tmp
            tmp = getFuel(tmp)

print total
