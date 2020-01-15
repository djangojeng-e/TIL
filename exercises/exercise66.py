tup = [x for x in range(1, 11)]
tup = tuple(tup)


def tuple_slicing(tup):
    print(tup[0:5])
    print(tup[5:])


tuple_slicing(tup)