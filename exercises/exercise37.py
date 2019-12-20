# This exercise requires to convert binary number to Decimal number

# Through the research, the function to convert binary back to decimal number is as below


def BinaryToDecimal(binary):

    binary1 = binary
    decimal = 0
    i = 0
    n = 0

    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i = i + 1

    return decimal

# Now, the input numbers will be turned into decimal first
# Then, they will be checked whether they are going to be divisible by 5.

binary_numbers = []
binary_decimal_dict = {}

while len(binary_numbers) < 4:
    user_input = int(input("Please enter your number "))
    if user_input not in binary_numbers:
        binary_numbers.append(user_input)
    for number in binary_numbers:
        decimal_number = BinaryToDecimal(number)
        binary_decimal_dict[number] = decimal_number

# completed collecting binary numbers for testing.

for binary_nums, decimal_nums in binary_decimal_dict.items():
    print(decimal_nums)
    print(str(binary_nums))
    if int(decimal_number) % 5 == 0:
        print(f'Yes. {binary_nums} is divisible by 5.')
    else:
        print(f'No. {binary_nums} is not divisible by 5.')

        
#
# Solution:
# value = []
# items=[x for x in raw_input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)
#
# print ','.join(value)