def duplicate_numbers(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y







# y is being the list that the duplicates have been removed from the first list. 

a = [1, 2, 3, 4, 3, 2, 1]

b = duplicate_numbers(a)
print(b)
print(duplicate_numbers(a))
y = duplicate_numbers(a)
