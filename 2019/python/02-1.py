#!/usr/bin/env python

memory = []

with open('../inputs/02.txt') as f:
    memory = map(int, f.read().split(','))

# patch:
memory[1] = 12
memory[2] = 2

#memory = [1,9,10,3,2,3,11,0,99,30,40,50]
#memory = [1,0,0,0,99]
#memory = [2,3,0,3,99]
#memory = [2,4,4,5,99,0]
#memory = [1,1,1,4,99,5,6,0,99]

pc = 0

while pc < len(memory):
    opcode = memory[pc]
    if opcode == 1:
        augend = memory[memory[pc + 1]]
        addend = memory[memory[pc + 2]]
        output = memory[pc + 3]
        sum = augend + addend
        #print('[{0}] = {1}'.format(output, sum))
        memory[output] = sum
    elif opcode == 2:
        multiplicand = memory[memory[pc + 1]]
        multiplier = memory[memory[pc + 2]]
        output = memory[pc + 3]
        product = multiplicand * multiplier
        #print('[{0}] = {1}'.format(output, product))
        memory[output] = product
    elif opcode == 99:
        break
    else:
        print('unhandled opcode={0}'.format(opcode))
    pc += 4

print memory[0]
