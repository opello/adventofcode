#!/usr/bin/env python

import hashlib

prefix = ''
number = 1

with open('../inputs/04.txt') as f:
   prefix = f.readlines()

prefix = prefix[0].rstrip()

while True:
   md5 = hashlib.md5()
   md5.update('{0}{1}'.format(prefix, number))

   if md5.hexdigest()[:5] == '00000':
      #print md5.hexdigest()
      print number
      break

   number += 1
