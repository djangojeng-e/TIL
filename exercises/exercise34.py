
word_list = []
while True:
    user_input = input("Please enter your words.")
    if user_input == '0':
        break
    else:
        word_list.append(user_input)

print(word_list)
word_list.sort()
print(word_list)

