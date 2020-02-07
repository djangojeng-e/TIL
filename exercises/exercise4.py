def previous_answer():
    user_number = int(input("Please enter your number : "))

    divisor = []

    for i in range(1,user_number):
        if user_number % i == 0:
            divisor.append(i)

    print(divisor)


# Another solution on 08/02/2020 starts here.

number = int(input('Please enter your number'))

number_list = [x for x in range(1, number)]
divisor_list = []

for num in number_list:
    if number % num == 0:
        divisor_list.append(num)

print(divisor_list)

