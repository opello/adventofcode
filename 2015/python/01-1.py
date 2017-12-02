#!/usr/bin/env python

floor = 0

with open('../inputs/01.txt') as f:
   while True:
      c = f.read(1)
      if not c:
         break
      if c == '(':
         floor += 1
      if c == ')':
         floor -= 1

print floor
