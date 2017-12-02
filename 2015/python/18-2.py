#!/usr/bin/env python

import PIL.Image

#lights = PIL.Image.new('RGB', (6, 6), 'black')
lights = PIL.Image.new('RGB', (100, 100), 'black')
pixels = lights.load()

def isOn(image, position):
   # Not the best boundary test...
   if min(position) < 0 or max(position) >= max(image.size):
      return False

   if image.getpixel(position) != (0, 0, 0):
      return True
   return False

def setOn(image, position):
   try:
      image.putpixel(position, (255, 255, 255))
   except:
      print image.size
      print position
      raise

def setOff(image, position):
   try:
      image.putpixel(position, (0, 0, 0))
   except:
      print image.size
      print position
      raise

def doStep(image1, image2, position):
   (x, y) = position

   neighborsLit = 0
   if isOn(image1, (x - 1, y - 1)):
      neighborsLit += 1
   if isOn(image1, (x, y - 1)):
      neighborsLit += 1
   if isOn(image1, (x + 1, y - 1)):
      neighborsLit += 1
   if isOn(image1, (x - 1, y)):
      neighborsLit += 1
   if isOn(image1, (x + 1, y)):
      neighborsLit += 1
   if isOn(image1, (x - 1, y + 1)):
      neighborsLit += 1
   if isOn(image1, (x, y + 1)):
      neighborsLit += 1
   if isOn(image1, (x + 1, y + 1)):
      neighborsLit += 1

   if isOn(image1, position) and neighborsLit in [2, 3]:
      setOn(image2, position)
   else:
      setOff(image2, position)

   if not isOn(image1, position) and neighborsLit == 3:
      setOn(image2, position)

   broken(image2)

def broken(image):
   setOn(image, (0, 0))
   setOn(image, (0, image.size[1] - 1))
   setOn(image, (image.size[0] - 1, 0))
   setOn(image, (image.size[0] - 1, image.size[1] - 1))

def display(image, dump=False):
   total = 0
   import sys
   for x in range(lights.size[0]):
      for y in range(lights.size[1]):
         if isOn(lights, (x, y)):
            if dump:
               sys.stdout.write('#')
            total += 1
         else:
            if dump:
               sys.stdout.write('.')
      if dump:
         sys.stdout.write('\n')
   print total

with open('../inputs/18.txt') as f:
   for (i, line) in enumerate(f):
      line = line.rstrip()
      for (j, char) in enumerate(line):
         if char == '#':
            setOn(lights, (i, j))
         else:
            setOff(lights, (i, j))

broken(lights)

display(lights, True)

for i in range(100):
   temp = lights.copy()
   for x in range(lights.size[0]):
      for y in range(lights.size[1]):
         doStep(temp, lights, (x, y))

display(lights, True)

#lights.save('18-100.png')
