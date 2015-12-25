#!/usr/bin/env python 

import re

data = dict()

with open('../inputs/16.txt') as f:
   for line in f:
      m = re.findall(r'(\w+):? (\d+)', line)
      for s in m:
         attributes = dict()
         for match in m:
            if match[0] == 'Sue':
               continue
            attributes[match[0]] = int(match[1])
         data[int(s[1])] = attributes

input = {
   'children': 3,
   'cats': 7,
   'samoyeds': 2,
   'pomeranians': 3,
   'akitas': 0,
   'vizslas': 0,
   'goldfish': 5,
   'trees': 3,
   'cars': 2,
   'perfumes': 1
}

matches = set()
for (sue, info) in data.iteritems():
   add = True

   for (k, v) in info.iteritems():
      if k in ['cats', 'trees']:
         if input[k] >= v:
            add = False
            break
      elif k in ['pomeranians', 'goldfish']:
         if input[k] <= v:
            add = False
            break
      elif input[k] != v:
         add = False
         break

   if add:
      matches.add(sue)

print matches
