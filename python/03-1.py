#!/usr/bin/env python

visited = []
x = 0
y = 0

# Count the first house.
visited += [(x,y)]

with open('../inputs/03.txt') as f:
   while True:
      c = f.read(1)
      if not c:
         break
      if c == '^':
         x += 1
      if c == 'v':
         x -= 1
      if c == '>':
         y += 1
      if c == '<':
         y -= 1

      visited += [(x,y)]

print len(set(visited))
