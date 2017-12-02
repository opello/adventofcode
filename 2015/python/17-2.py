#!/usr/bin/env python 

import re
import itertools

containers = []

with open('../inputs/17.txt') as f:
   for line in f:
      m = re.findall(r'(\d+)', line)
      containers.append(int(m[0]))

combinations = dict()
minimum = 0
for i in range(len(containers)):
   for c in itertools.combinations(containers, i):
      if sum(c) == 150:
         if minimum == 0 or len(c) <= minimum:
            minimum = len(c)
            if len(c) not in combinations:
               combinations[len(c)] = []
            combinations[len(c)].append(c)

print len(combinations[minimum]) 
