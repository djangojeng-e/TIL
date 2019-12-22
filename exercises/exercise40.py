user_input = input("Please enter your sentence : ")

sentence = user_input.split(' ')

Upper_case = 0
Lower_case = 0

for word in sentence:
    for letter in word:
        if letter.isalpha():
            if letter.isupper():
                Upper_case += 1
            elif letter.islower():
                Lower_case += 1

print('UPPER CASE ', Upper_case)
print('LOWER CASE ', Lower_case)