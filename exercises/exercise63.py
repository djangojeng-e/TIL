def square_numbers(n1, n2):
    squares = [x ** 2 for x in range(n1, n2 + 1)]
    print(squares[0:5])

square_numbers(1, 20)