#!/usr/bin/env python

import re

length = 0
unEscapeLength = 0
escapeLength = 0

with open('../inputs/08.txt') as f:
   for line in f:
      line = line.rstrip()
      length += len(line)
      unEscapeLength += len(line[1:-1].decode('string_escape'))
      escapeLength += len('"{0}"'.format(re.escape(line)))

print (length - unEscapeLength)
print (escapeLength - length)
