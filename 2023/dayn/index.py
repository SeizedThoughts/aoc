import os
import re
import pyperclip

# re.split('', line)
# re.sub('^', '', line)
# re.sub('$', '', line)

bs = [[
    l.strip()
for l in b.split('\n')] for b in re.split('\n{2,}', open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r').read().strip())]

flag = 0

for bi in range(len(bs)):
    # if bi == 0:
    b = bs[bi]
    for i in range(len(b)):
        l = b[i]
        
        
        

pyperclip.copy(flag)

print(flag)