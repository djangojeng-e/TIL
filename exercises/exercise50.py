
# Print built-in functions documents for abs()
print(abs.__doc__)

# Print built-in functions documents for int()

print(int.__doc__)

# Print built-in functions documents for input()

print(input.__doc__)


# Add one own function and prints out documentation.

def square_number(n):
    '''
    This function returns square number of the number input.

    :param n:
    :return:
    '''

    squared_num = n ** 2

    return squared_num


print(square_number.__doc__)