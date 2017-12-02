#!/usr/bin/env python 

import re

def look_and_say(s):
   pieces = re.findall(r'((\d)\2*)', s)

   output = ''
   for piece in pieces:
      l = len(piece[0])
      if l > 0:
         output += str(l)
         output += str(piece[1])

   return output

with open('../inputs/10.txt') as f:
   for line in f:
      line = line.rstrip()

      temp = line
      for i in range(50):
         temp = look_and_say(temp)
      
      print len(temp)
