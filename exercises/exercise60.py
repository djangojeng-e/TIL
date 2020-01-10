def dictionary(n1, n2):
    dict = {}
    for number in range(n1, n2 + 1):
        dict[number] = number ** 2

    for key in dict.keys():
        print(key)

dictionary(1, 20)
