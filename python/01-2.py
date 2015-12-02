#!/usr/bin/env python

floor = 0
chars = 0

with open('../inputs/01.txt') as f:
   while True:
      c = f.read(1)
      if not c:
         break
      chars += 1
      if c == '(':
         floor += 1
      if c == ')':
         floor -= 1
      if floor < 0:
         print chars
         break
