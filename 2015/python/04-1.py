#!/usr/bin/env python

import hashlib

prefix = ''
number = 1

with open('../inputs/04.txt') as f:
   prefix = f.readlines()

prefix = prefix[0].rstrip()

md5 = hashlib.md5()
md5.update(prefix)

while True:
   m = md5.copy()
   m.update(str(number))

   if m.hexdigest()[:5] == '00000':
      print number
      break

   number += 1
