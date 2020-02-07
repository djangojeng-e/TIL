def previous_solution():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []      # creates list of common elements.
    for a in a:
        if a in b:
            if a in c:
                continue
            else:
                c.append(a)

    print(c)


# Another solution on 08/02/2020 starts here.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for nums in a:
    if nums in b:
        c.append(nums)


c = [x for x in a if x in b]
