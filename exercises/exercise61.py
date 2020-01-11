def dictionary(n1, n2):
    dict ={}
    for number in range(n1, n2+1):
        dict[number] = number ** 2
    for values in dict.values():
        print(values)

dictionary(1, 20)