def previous_answer():
#1.
    num1 = int(input("Please enter your number!"))

    if num1 % 2 == 0:
        print("Your number is EVEN number!")
    else:
        print("Your number is ODD number!")

    #2.

    num2 = int(input("Please enter second number!"))
    num3 = int(input("Please enter third number!"))

    if num2 % num3 == 0:
        print("second number is divisible by third number perfectly!")
    else:
        print("Second number is not divisible by third number!")


# Current answer starts here.

num = int(input('Please enter your number'))
if num % 2 == 0:
    if num % 4 == 0:
        print('It is an even number and also a multiple of 4')
    else:
        print('It is an even number')
else:
    print('It is an odd number')






