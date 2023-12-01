import os
import pyperclip

[b1] = [[line for line in block.split('\n')] for block in open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r').read().split('\n\n')]

numbers = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

total = 0

flag = 'None'

for i in range(len(b1)):
    line = b1[i]

    num = 0

    found = False
    while not found:
        for j in range(len(numbers)):
            number = numbers[j]
            if line.startswith(number):
                if j < 9:
                    num += (j + 1) * 10
                else:
                    num += 10 * int(number)
                found = True
                break
        
        line = line[1:]

        if line == '':
            break
    
    found = False
    while not found:
        for j in range(len(numbers)):
            number = numbers[j]
            if line.endswith(number):
                if j < 9:
                    num += (j + 1)
                else:
                    num += int(number)
                found = True
                break
        
        line = line[:-1]

        if line == '':
            break
    
    if num % 10 == 0:
        num += int(num / 10)
    
    total += int(num)
    

flag = str(total)

pyperclip.copy(flag)

print(flag)