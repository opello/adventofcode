#!/usr/bin/env python

import re

instructions = []

def doOperation(operator, operands):
   if operator == '':
      return operands[0]
   elif operator == 'NOT':
      return ~operands[0]
   elif operator == 'AND':
      return operands[0] & operands[1]
   elif operator == 'OR':
      return operands[0] | operands[1]
   elif operator == 'LSHIFT':
      return operands[0] << operands[1]
   elif operator == 'RSHIFT':
      return operands[0] >> operands[1]
   else:
      raise ValueError

def isInt(value):
   try:
      int(value)
      return True
   except ValueError:
      return False

with open('../inputs/07.txt') as f:
   for line in f:
      line = line.rstrip()
      expression = re.split(r' -> ', line)
      operands = re.split(r' ', expression[0])
      output = expression[1]

      # Pass through operation.
      operator = ''
      operandsCount = len(operands)
      # Binary operation.
      if operandsCount == 3:
         operator = operands[1]
      # Unary operation.
      elif operandsCount == 2:
         operator = operands[0]

      if operator != '':
         operands.remove(operator)

      for i in range(len(operands)):
         if isInt(operands[i]):
            operands[i] = int(operands[i])

      instructions += [(output, operator, operands)]

state = {}
while 'a' not in state.keys():
   for i in instructions:
      output, operator, operands = i

      cont = False

      for i in range(len(operands)):
         if isInt(operands[i]):
            continue
         elif operands[i] in state.keys():
            operands[i] = state[operands[i]]
            continue
         else:
            cont = True
            break
      
      if cont:
         continue

      state[output] = doOperation(operator, operands)

      if output == 'b':
         state[output] = 16076

print state['a']
