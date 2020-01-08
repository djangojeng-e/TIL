print("Please enter two numbers to set the range")
print()

starting_number = int(input("Please enter the starting number of range"))
ending_number = int(input("Please enter the ending number of range"))


def square_dict(n1, n2):
    dictionary = {}  # create an empty dictionary to store square values of numbers.
    for number in range(n1, n2 + 1):
        dictionary[number] = number ** 2

    print(dictionary)

square_dict(starting_number, ending_number)

