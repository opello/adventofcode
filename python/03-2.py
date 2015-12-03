#!/usr/bin/env python

visited = []
x1 = 0
y1 = 0
x2 = 0
y2 = 0

# Count the first house.
visited += [(x1,y1)]
visited += [(x2,y2)]

roboFlag = False

with open('../inputs/03.txt') as f:
   while True:
      c = f.read(1)
      if not c:
         break

      if roboFlag == False:
         if c == '^':
            x1 += 1
         if c == 'v':
            x1 -= 1
         if c == '>':
            y1 += 1
         if c == '<':
            y1 -= 1

         visited += [(x1,y1)]
         roboFlag = True

      else:
         if c == '^':
            x2 += 1
         if c == 'v':
            x2 -= 1
         if c == '>':
            y2 += 1
         if c == '<':
            y2 -= 1

         visited += [(x2,y2)]
         roboFlag = False

print len(set(visited))
