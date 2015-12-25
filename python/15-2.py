#!/usr/bin/env python 

import re

data = dict()

with open('../inputs/15.txt') as f:
   for line in f:
      m = re.match(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
      (name, c, d, f, t, C) = m.groups()
      data[name] = (int(c), int(d), int(f), int(t), int(C))

maxScore = 0
for i in range(100):
   for j in range(100):
      for k in range(100):
         l = 100 - i - j - k

         c = (data['Sprinkles'][0] * i) + \
             (data['PeanutButter'][0] * j) + \
             (data['Frosting'][0] * k) + \
             (data['Sugar'][0] * l)
         d = (data['Sprinkles'][1] * i) + \
             (data['PeanutButter'][1] * j) + \
             (data['Frosting'][1] * k) + \
             (data['Sugar'][1] * l)
         f = (data['Sprinkles'][2] * i) + \
             (data['PeanutButter'][2] * j) + \
             (data['Frosting'][2] * k) + \
             (data['Sugar'][2] * l)
         t = (data['Sprinkles'][3] * i) + \
             (data['PeanutButter'][3] * j) + \
             (data['Frosting'][3] * k) + \
             (data['Sugar'][3] * l)
         C = (data['Sprinkles'][4] * i) + \
             (data['PeanutButter'][4] * j) + \
             (data['Frosting'][4] * k) + \
             (data['Sugar'][4] * l)

         if C != 500:
            continue

         if min(c, d, f, t) <= 0:
            continue

         score = c * d * f * t;
         if maxScore == 0 or score > maxScore:
            maxScore = score

print maxScore
