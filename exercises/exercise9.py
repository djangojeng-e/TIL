import random 


tries = 0              

while True:
    generate_number = random.randint(1,9)
    user_number = input("Please enter your number : ")
    if user_number == 'exit':
        break
    elif generate_number == int(user_number):
        print("You have guessed exactly right number.")
        tries += 1
    elif generate_number < int(user_number):
        print("You have guessed too low.")
        tries += 1
    elif generate_number > int(user_number):
        print("You have guessed too high.")
        tries += 1
    

print(tries)


