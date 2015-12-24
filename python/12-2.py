#!/usr/bin/env python

import json

total = 0
def sumNotRed(data):
   global total

   if type(data) is int:
      total += data
      return

   if type(data) is dict:
      for (k, v) in data.iteritems():
         if v == 'red':
            return

      for (k, v) in data.iteritems():
         sumNotRed(v)

   elif type(data) is list:
      for o in data:
         sumNotRed(o)

data = {}
with open('../inputs/12.txt') as f:
   data = json.load(f)

sumNotRed(data)
print total
