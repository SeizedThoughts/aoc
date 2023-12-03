import os
import pyperclip

[
    b1
] = [[
    (line)
for line in block.split('\n')] for block in open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r').read().split('\n\n')]

flag = 'None'

for i in range(len(b1)):
    line = b1[i]
    
    
    

pyperclip.copy(flag)

print(flag)