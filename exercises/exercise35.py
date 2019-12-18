word_list = []

while True:
    user_input = input("Please enter your words.")
    if user_input == '0':
        break
    else:
        capitalised_input = user_input.upper()
        word_list.append(capitalised_input)

for word in word_list:
    print(word, sep=" ")

print(" ".join(word_list))

