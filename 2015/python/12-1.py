#!/usr/bin/env python

import json

total = 0

def sumer(s):
   global total
   total += int(s)

data = {}
with open('../inputs/12.txt') as f:
   data = json.load(f, parse_int=sumer)

print total
