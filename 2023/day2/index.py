import os
import pyperclip

[b1] = [[line for line in block.split('\n')] for block in open(os.path.dirname(os.path.abspath(__file__)) + '/input.txt', 'r').read().split('\n\n')]

flag = 'None'

t = 0

for i in range(len(b1)):
    line = b1[i]

    game = [[(int(color.split(' ')[0]), color.split(' ')[1]) for color in group.split(', ')] for group in line[(line.index(': ') + 2):].split('; ')]

    colors = {
        'blue': 0,
        'red': 0,
        'green': 0
    }

    for rounds in game:
        for color in rounds:
            if colors[color[1]] < color[0]:
                colors[color[1]] = color[0]

    t += colors['blue'] * colors['red'] * colors['green']

flag = t

pyperclip.copy(flag)

print(flag)