import random

head_number = int(input("Please enter your number between 0 and 100 : "))
guess_number = 0 
tries = 0

while head_number != guess_number:
    guess_number = random.randint(0, 100)
    if head_number < 0 or head_number > 100:
        print("Please enter a vaild number")
        head_number = int(input("Please enter a  valid number : "))
    else:
        tries += 1


print(f'computer tried {tries} times to guess your number. your number was {head_number}')



