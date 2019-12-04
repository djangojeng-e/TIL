number_one = int(input("Please Enter the first number. "))
number_two = int(input("Please Enter the second number. "))
number_three = int(input("Please Enter the third number. "))

if number_one > number_two:
    if number_two > number_three:
        print(f'number one {number_one} is the biggest number.')
elif number_two > number_one:
    if number_one > number_three:
        print(f'number two {number_two} is the biggest number.')
elif number_three > number_two:
    if number_two > number_one:
        print(f'number three {number_three} is the biggest number.')

        
