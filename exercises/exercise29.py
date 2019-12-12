

def dictionary():
    number_dictionary = {}
    integral_number = int(input("Enter your number : "))
    for numbers in range(1, integral_number + 1):
        number_dictionary[numbers] = numbers * numbers

    print(number_dictionary)

dictionary()
