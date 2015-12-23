#!/usr/bin/env python 
import itertools

cities = set()
edges = dict()
total = 0

with open('../inputs/09.txt') as f:
   for line in f:
      line = line.rstrip()
      (c1, _, c2, _, d) = line.split()

      cities.add(c1)
      cities.add(c2)

      if c1 not in edges:
          edges[c1] = dict()
      if c2 not in edges:
          edges[c2] = dict()

      edges[c1][c2] = int(d)
      edges[c2][c1] = int(d)

for route in itertools.permutations(cities):
   distance = 0
   for i in range(len(route) - 1):
      distance += edges[route[i]][route[i + 1]]

   if total == 0 or total > distance:
      total = distance

print total
