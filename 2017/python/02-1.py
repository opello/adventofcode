#!/usr/bin/env python 

checksum = 0

with open('../inputs/02.txt') as f:
   for line in f:
       line = map(int, line.rstrip().split())
       cs = max(line) - min(line)
       checksum += cs

print checksum
