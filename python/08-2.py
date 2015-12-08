#!/usr/bin/env python

import re

length = 0
newLength = 0

with open('../inputs/08.txt') as f:
   for line in f:
      line = line.rstrip()
      length += len(line)
      newLength += len('"{0}"'.format(re.escape(line)))

print (newLength - length)
