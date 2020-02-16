import random
number_list = [x for x in range(100, 201) if x % 2 == 0]

random_sample = random.sample(number_list, 5)

print(random_sample)