#!/usr/bin/env python

import re
import PIL.Image

lights = PIL.Image.new('RGB', (1000, 1000), 'black')
pixels = lights.load()

def isOn(position):
   if pixels[position[0], position[1]] != (0, 0, 0):
      return True
   return False

def setOn(position):
   pixels[position[0], position[1]] = (255, 255, 255)

def setOff(position):
   pixels[position[0], position[1]] = (0, 0, 0)

def doCommand(command, position):
   if command == 'turn on':
      setOn(position)
   elif command == 'turn off':
      setOff(position)
   elif command == 'toggle':
      if isOn(position):
         setOff(position)
      else:
         setOn(position)
   else:
      raise ValueError

with open('../inputs/06.txt') as f:
   for line in f:
      commands = re.findall(r'turn on|turn off|toggle', line)
      command = commands[0]

      numbers = re.findall(r'\d+', line)
      x1 = int(numbers[0])
      y1 = int(numbers[1])
      x2 = int(numbers[2])
      y2 = int(numbers[3])

      for x in range(x1, x2 + 1):
         for y in range(y1, y2 + 1):
            doCommand(command, (x, y))

total = 0
for x in range(lights.size[0]):
   for y in range(lights.size[1]):
      if isOn((x, y)):
         total += 1

#lights.save('06-1.png')
print total
