def square_dict(n1, n2):
    dict = {}
    for number in range(n1, n2+1):
        dict[number] = number ** 2
        print(dict)

square_dict(1, 20)