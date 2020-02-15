import random

number_list = [x for x in range(100, 201)]

print(number_list)

random_list = random.sample(number_list, 5)

print(random_list)