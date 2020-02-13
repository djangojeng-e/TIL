import random

even_numbers = [x for x in range(0, 11) if x % 2 == 0]
random_even_number = random.choice(even_numbers)

print(random_even_number)

# One line solution

print(random.choice([i for i in range(11) if i % 2 == 0]))

