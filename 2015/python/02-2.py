#!/usr/bin/env python

import re

total = 0

with open('../inputs/02.txt') as f:
   for line in f:
      # data is like "1x2x3"
      matches = re.split("(\d+)", line)

      # 7 = 3 matches + 2 empty matches + 2 x characters
      # The empty matches are because of the expression matches the begin and
      # end of the string.
      if len(matches) == 7:
         l = int(matches[1])
         w = int(matches[3])
         h = int(matches[5])

         dimensions = [l, w, h]
         dimensions.sort()

         shortPerimiter = (2 * dimensions[0]) + (2 * dimensions[1])
         volume = l * w * h

         total += shortPerimiter + volume
      else:
         print "Error: did not find 3 matches '%s'" % (line)

print total
