import os
import pyperclip

[
    b1
] = [[
    (line)
for line in block.split('\n')] for block in open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r').read().split('\n\n')]

flag = 0

for i in range(len(b1)):
    line = b1[i]

    for j in range(len(line)):
        c = line[j]
        if(c == '*'):
            gear = set()
            if(i > 0 and j > 0):
                if(ord('0') <= ord(b1[i - 1][j - 1]) <= ord('9')):
                    k = j - 1
                    while ord('0') <= ord(b1[i - 1][k]) <= ord('9'):
                        k -= 1
                    k += 1

                    gear.add((i - 1, k))

            if(i > 0):
                if(ord('0') <= ord(b1[i - 1][j]) <= ord('9')):
                    k = j
                    while ord('0') <= ord(b1[i - 1][k]) <= ord('9'):
                        k -= 1
                    k += 1

                    gear.add((i - 1, k))

            if(i > 0 and j < len(line) - 1):
                if(ord('0') <= ord(b1[i - 1][j + 1]) <= ord('9')):
                    k = j + 1
                    while ord('0') <= ord(b1[i - 1][k]) <= ord('9'):
                        k -= 1
                    k += 1

                    gear.add((i - 1, k))

            if(i < len(b1) - 1 and j > 0):
                if(ord('0') <= ord(b1[i + 1][j - 1]) <= ord('9')):
                    k = j - 1
                    while ord('0') <= ord(b1[i + 1][k]) <= ord('9'):
                        k -= 1
                    k += 1

                    gear.add((i + 1, k))

            if(i < len(b1) - 1):
                if(ord('0') <= ord(b1[i + 1][j]) <= ord('9')):
                    k = j
                    while ord('0') <= ord(b1[i + 1][k]) <= ord('9'):
                        k -= 1
                    k += 1

                    gear.add((i + 1, k))

            if(i < len(b1) - 1 and j < len(line) - 1):
                if(ord('0') <= ord(b1[i + 1][j + 1]) <= ord('9')):
                    k = j + 1
                    while ord('0') <= ord(b1[i + 1][k]) <= ord('9'):
                        k -= 1
                    k += 1

                    gear.add((i + 1, k))

            if(j < len(line) - 1):
                if(ord('0') <= ord(b1[i][j + 1]) <= ord('9')):
                    k = j + 1
                    while ord('0') <= ord(b1[i][k]) <= ord('9'):
                        k -= 1
                    k += 1

                    gear.add((i, k))

            if(j > 0):
                if(ord('0') <= ord(b1[i][j - 1]) <= ord('9')):
                    k = j - 1
                    while ord('0') <= ord(b1[i][k]) <= ord('9'):
                        k -= 1
                    k += 1

                    gear.add((i, k))
            
            if(len(gear) == 2):
                sub = 1
                for p in list(gear):
                    num = ''
                    k = p[1]
                    while k < len(b1[0]) and ord('0') <= ord(b1[p[0]][k]) <= ord('9'):
                        num += b1[p[0]][k]

                        k += 1

                    sub *= int(num)
                
                
                flag += sub

pyperclip.copy(flag)

print(flag)