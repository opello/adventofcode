#!/usr/bin/env python 

checksum = 0

with open('../inputs/02.txt') as f:
   for line in f:
       line = map(int, line.rstrip().split())
       evenDivisors = []
       for n in line:
           for m in line:
               if m == n:
                   continue
               if n % m == 0:
                   evenDivisors = [n, m]
                   break
       cs = max(evenDivisors) / min(evenDivisors)
       checksum += cs

print checksum
