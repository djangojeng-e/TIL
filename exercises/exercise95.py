import random
number_list = [x for x in range(1, 1001) if x % 5 == 0 and x % 7 == 0]

random_list = random.sample(number_list, 5)


print(number_list)

print(random_list)

five_list = random.sample([x for x in range(1, 1001) if x % 5 == 0 and x % 7 ==0], 5)

print(five_list)