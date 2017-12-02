#!/usr/bin/env python 

import re
import itertools

people = set()
relationships = dict()
total = 0

with open('../inputs/13.txt') as f:
   for line in f:
      m = re.match(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', line)

      (p1, operand, value, p2) = m.groups()

      value = int(value)
      if operand == 'lose':
         value = -value;

      people.add(p1)
      people.add(p2)

      if p1 not in relationships:
         relationships[p1] = dict()
      if p2 not in relationships:
         relationships[p2] = dict()

      relationships[p1][p2] = value

# Add myself.
relationships['myself'] = dict()
for p in people:
   relationships['myself'][p] = 0
   relationships[p]['myself'] = 0
people.add('myself')

for arrangement in itertools.permutations(people):
   components = []
   happiness = 0
   for i in range(-1, len(arrangement) - 1):
      p1 = arrangement[i]
      p2 = arrangement[i + 1]

      happiness += relationships[p1][p2]
      happiness += relationships[p2][p1]

   if total == 0 or total < happiness:
      total = happiness

print total
