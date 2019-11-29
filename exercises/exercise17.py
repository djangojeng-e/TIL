import random

answer = []

while len(answer) <= 3:
    random_number = random.randint(1, 9)
    if random_number not in answer:
        answer.append(random_number)

print(answer)
cows = 0
tries = 0

while cows != 4:
    guess = input("Please enter your number.")
    tries = tries + 1
    guesses = []
    for numbers in guess:
        if numbers not in guesses:
            numbers = int(numbers)
            guesses.append(numbers)

    cows = 0
    bulls = 0

    for i in range(0, 4):
        if answer[i] == guesses[i]:
            cows += 1
        else:
            bulls += 1

    print(f'{cows} cows, {bulls} bulls at {tries} tries')


print('You got 4 bulls')


print(guesses)
