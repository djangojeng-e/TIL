def square_tuples(n1, n2):
    square_list = [numbers ** 2 for numbers in range(n1, n2 + 1)]
    square_list = tuple(square_list)
    print(square_list)


square_tuples(1, 20)
