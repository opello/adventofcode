#!/usr/bin/env python 

import re
import operator

data = dict()

with open('../inputs/14.txt') as f:
   for line in f:
      m = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)

      (name, speed, duty, rest) = m.groups()
      data[name] = (int(speed), int(duty), int(rest))

time = 2503
position = {}
for (name, info) in data.iteritems():
   cycles = time / (info[1] + info[2])
   remainder = time % (info[1] + info[2])
   if remainder > info[1]:
      cycles += 1

   position[name] = info[0] * info[1] * cycles

print max(position.iteritems(), key=operator.itemgetter(1))
