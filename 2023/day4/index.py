import os
import pyperclip

[
    b1
] = [[
    ([
        [int(g) for g in b.split(' ')]
    for b in line.split(' | ')])
for line in block.split('\n')] for block in open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r').read().split('\n\n')]

copies = [1] * len(b1)

flag = 0

for i in range(len(b1)):
    line = b1[i]
    
    ptr = i + 1
    for n in line[0]:
        if n in line[1]:
            if(ptr < len(b1)):
                copies[ptr] += copies[i]
                ptr += 1
    
flag = sum(copies)

pyperclip.copy(flag)

print(flag)