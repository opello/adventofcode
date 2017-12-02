#!/usr/bin/env python

length = 0
escapeLength = 0

with open('../inputs/08.txt') as f:
   for line in f:
      line = line.rstrip()
      length += len(line)
      escapeLength += len(line[1:-1].decode('string_escape'))

print (length - escapeLength)
