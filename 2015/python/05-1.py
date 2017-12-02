#!/usr/bin/env python

import re

total = 0

reVowels = r'[aeiou]'
vowelCount = 3
reDoubleLetters = r'.*([a-z])\1.*'
reBadStrings = r'(ab|cd|pq|xy)'

doubleLetters = re.compile(reDoubleLetters)

with open('../inputs/05.txt') as f:
   for line in f:
      vowels = re.findall(reVowels, line)
      if len(vowels) < vowelCount:
         continue

      if not doubleLetters.match(line):
         continue

      badStrings = re.findall(reBadStrings, line)
      if len(badStrings) > 0:
         continue

      total += 1

print total
