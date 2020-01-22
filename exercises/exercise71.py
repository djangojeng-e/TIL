number_list = [x for x in range(1, 21)]

print(number_list)
filtered_list = filter(lambda x: x%2==0, number_list)

filtered_list = list(filtered_list)
print(filtered_list)

square_list = map(lambda x: x**2, filtered_list)

square_list = list(square_list)
print(square_list)

# filter(func, iterable)
# map(func, iterable) 