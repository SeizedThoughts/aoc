import os
import math
import re
import pyperclip

# re.split('', l)
# re.sub('^', '', l)
# re.sub('$', '', l)

bs = [[
    [int(re.sub('\D+', '', l.strip()))]
for l in b.split('\n')] for b in re.split('\n{2,}', open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r').read().strip())]

flag = 1

for p in [(bs[0][0][i], bs[0][1][i]) for i in range(len(bs[0][0]))]:
    a = 1
    b = -p[0]
    c = p[1]

    x1 = math.ceil((-b + math.sqrt((b * b) - (4 * a * c))) / 2 / a) - 1
    x2 = math.floor((-b - math.sqrt((b * b) - (4 * a * c))) / 2 / a) + 1

    flag = x1 - x2 + 1
        

pyperclip.copy(flag)

print(flag)