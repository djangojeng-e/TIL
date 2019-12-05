# f = open('sowpods.txt', 'r')
#
#
# f.close()

import random


with open('sowpods.txt', 'r') as f:
    lines = f.read().splitlines()

word_list = list(lines)
print(word_list)

print(random.choice(word_list)) # Picking up one word here.
