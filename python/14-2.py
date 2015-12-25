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
position = dict()
leads = dict()

for i in range(1, time + 1):
   for (name, info) in data.iteritems():
      (speed, duty, rest) = info
      
      moving = False
      cycles = time / (duty + rest)
      remainder = i % (duty + rest)
      
      if remainder > duty:
         cycles += 1

      if remainder != 0 and remainder <= duty:
         moving = True

      if name not in position:
         position[name] = 0

      if moving:
         position[name] += speed

   lead = max(position.iteritems(), key=operator.itemgetter(1))

   for (n, p) in position.iteritems():
      if n not in leads:
         leads[n] = 0

      if p == lead[1]:
         leads[n] += 1
   
print leads
print max(leads.iteritems(), key=operator.itemgetter(1))
