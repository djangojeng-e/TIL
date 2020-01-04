def string_to_sum():
    string_one = input('Please enter first number')
    string_two = input('Please enter second number')
    string_one_integer = int(string_one)
    string_two_integer = int(string_two)
    sum = string_one_integer + string_two_integer
    print(f'sum( {string_one} + {string_two} ) = {sum}')


string_to_sum()


