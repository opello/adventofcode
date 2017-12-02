#!/usr/bin/env python

import re
import string
import math

total = 0

# TODO: require runs {abc, def, etc.}
reBadStrings = r'(i|o|l)'
reDoubleLetters = r'(([a-z])\2)'

doubleLetters = re.compile(reDoubleLetters)

alphabet = string.ascii_lowercase

def incr(s):
   letters = []
   for (i, l) in enumerate(s):
      letters.append(l)

   letters.reverse()

   number = 0
   for (i, l) in enumerate(letters):
      letterValue = ord(l) - ord('a')
      letterValue *= (len(alphabet) ** i)
      number += letterValue

   number += 1

   newLetters = []
   while True:
      remainder = number % len(alphabet)
      number = number / len(alphabet)
      letterValue = remainder + ord('a')
      newLetters.append(chr(letterValue))

      if number == 0:
         break

   # "Zero pad" the result with leading 'a's.
   for i in range(len(newLetters), 8):
      newLetters.append('a')

   newLetters.reverse()
   return ''.join(newLetters)

with open('../inputs/11.txt') as f:
   for line in f:
      line = line.rstrip()

      flag = False
      while True:
         line = incr(line)

         hasRun = False
         for (i, l) in enumerate(line):
            # Stop at the third-to-last character.
            if i > (len(line) - 1 - 2):
               break

            a = ord(l);
            b = ord(line[i+1]);
            c = ord(line[i+2]);

            if b == (a + 1) and c == (b + 1):
               hasRun = True
               break
            else:
               continue

         if not hasRun:
            #print '{0}: no run found'.format(line)
            continue

         badPasswords = re.findall(reBadStrings, line)
         if len(badPasswords) > 0:
            #print '{0}: includes {1}'.format(line, reBadStrings)
            continue

         matches = doubleLetters.findall(line)
         pairs = []
         for (s, l) in matches:
            pairs.append(s)

         if len(set(pairs)) < 2:
            #print '{0}: not enough pairs'.format(line)
            continue

         print line

         if flag == True:
            break

         flag = True
