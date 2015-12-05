#!/usr/bin/env python

import re

total = 0

niceDigraphs = re.compile(r'.*([a-z][a-z]).*\1.*')
niceTrigraphs = re.compile(r'.*([a-z])[a-z]\1.*')

with open('../inputs/05.txt') as f:
   for line in f:
      line = line.rstrip()

      if not niceDigraphs.match(line):
         continue

      if not niceTrigraphs.match(line):
         continue

      total += 1

print total
