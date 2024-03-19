import numpy as np
import matplotlib.pyplot as plt

dim = 100
iters = 200

white = u'\u2588'
black = u'\u2591'

initial = np.zeros(dim)
final = np.zeros(dim)

numbers = 0


def wrap(i):
    result = 0
    if (i < 0):
        result = wrap(i + dim)
    elif (i >= dim):
        result = wrap(i - dim)
    else:
        result = i
    return result


def printline(a):
    for element in list(a):
        if element == 1:
            character = white
        else:
            character = black
        if (numbers == 1):
            character = str(element) + " "
        print(character, end="")

    print("")


# initilize
initial[50] = 1
initial[51] = 1

printline(initial)

for t in range(iters):
    for i in range(len(initial)):
        if (initial[i] == 1):
            if (initial[wrap(i-1)] + initial[(wrap(i+1))] + initial[wrap(i-2)] + initial[(wrap(i+2))] == 4):
                final[i] = 0
            else:
                final[i] = 1
        elif (initial[i] == 0):
            if (initial[wrap(i-1)] + initial[(wrap(i+1))] == 2):
                final[i] = 1
            elif (initial[wrap(i-1)] + initial[(wrap(i-2))] == 2):
                final[i] = 1
            elif (initial[wrap(i+1)] + initial[(wrap(i+2))] == 2):
                final[i] = 1
            else:
                final[i] = 0
    printline(final)
    initial = final
    final = np.zeros(dim)
