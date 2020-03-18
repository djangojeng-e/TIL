# filter() - Function lets us keep the values that satisfy some conditional logic
from functools import reduce

set_one = set(filter(lambda x: x > 4, range(7)))
print(set_one)

# This filters in the elements from 0 to 6 that are greater than the number 4

# map()
# This function applies a function to each element in the iterable

set_two = set(map(lambda x: x**3, range(7)))
print(set_two)
# This calculates the cube for each element in the range 0 to 6 and stores them in a set

# reduce() function reduces a sequence pair-wise,
# repeatedly until we arrive at a single value

reduce_one = reduce(lambda x, y: y - x, [1, 2, 3, 4, 5])
print(reduce_one)


