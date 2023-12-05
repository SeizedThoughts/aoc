import os
import re
import pyperclip

# re.split('', line)
# re.sub('^', '', line)
# re.sub('$', '', line)

bs = [[
    [int(j) for j in l.strip().split(' ')]
for l in b.split('\n')[1:]] for b in re.split('\n{2,}', open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r').read().strip())]

def fragment(r1, r2):
    ranges = []
    if r1[0] < r2[0] and r1[1] >= r2[0]:
        ranges.append((r1[0], r2[0] - 1))
        r1 = (r2[0], r1[1])
    
    if r1[1] > r2[1] and r1[0] <= r2[1]:
        ranges.append((r2[1] + 1, r1[1]))
        r1 = (r1[0], r2[1])
    
    ranges.append(r1)

    return ranges

locs = []

flag = 0

for bi in range(len(bs)):
    b = bs[bi]
    if(bi == 0):
        for i in range(0, len(b[0]), 2):
            locs.append([(b[0][i], b[0][i] + b[0][i + 1] - 1)])
    else:
        for j in range(len(locs)):
            for i in range(1, len(b)):
                l = b[i]

                new_ranges = []
                for r in locs[j]:
                    new_ranges += fragment(r, (l[1], l[1] + l[2] - 1))
                locs[j] = new_ranges
                
            new_ranges = []
            for i in range(0, len(b)):
                l = b[i]

                old_ranges = locs[j].copy()
                for r in old_ranges:
                    if l[1] <= r[0] < (l[1] + l[2]):
                        new_ranges.append(((l[0] + (r[0] - l[1])), (l[0] + (r[1] - l[1]))))
                        locs[j].remove(r)
            locs[j] += new_ranges

flag = min([min([k[0] for k in r]) for r in locs])

pyperclip.copy(flag)

print(flag)