#!/usr/bin/env python

def test(memory, noun, verb):
    pc = 0
    m = memory[:]
    if noun is not None:
        m[1] = noun
    if verb is not None:
        m[2] = verb

    while pc < len(m):
        opcode = m[pc]
        if opcode == 1:
            augend = m[m[pc + 1]]
            addend = m[m[pc + 2]]
            output = m[pc + 3]
            sum = augend + addend
            #print('[{0}] = {1}'.format(output, sum))
            m[output] = sum
        elif opcode == 2:
            multiplicand = m[m[pc + 1]]
            multiplier = m[m[pc + 2]]
            output = m[pc + 3]
            product = multiplicand * multiplier
            #print('[{0}] = {1}'.format(output, product))
            m[output] = product
        elif opcode == 99:
            break
        else:
            print('unhandled opcode={0}'.format(opcode))
        pc += 4

    return m[0]

memory = []

with open('../inputs/02.txt') as f:
    memory = map(int, f.read().split(','))

answer = 19690720
noun = 0
verb = 0

for i in range(0, 100):
    for j in range(0, 100):
        if test(memory, i, j) == answer:
            noun = i
            verb = j
            break
    else:
        continue
    break

final = 100 * noun + verb
print('noun={0} verb={1} answer={2}'.format(noun, verb, final))
