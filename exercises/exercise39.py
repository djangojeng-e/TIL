user_input = input("Please enter your sentence. : ")

user_sentence = user_input.split(' ')

LETTERS = 0
DIGITS = 0

for words in user_sentence:
    for word in words:
        if word.isdigit():
            DIGITS += 1
        elif word.isalpha():
            LETTERS +=1

print("LETTERS : ", LETTERS)
print("DIGITS :", DIGITS)


