if __name__ == '__main__':
    print("Welcome to hangman!!")
    word = "EVAPORATE"
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = input("Guess letter: ")
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!!")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            guessed[index] = letter.upper()
            word[index] = '_'
        else:
            print(''.join(guessed))
            if letter is not '':
                lstGuessed.append(letter.upper())
            letter = input("guess letter: ")
        if '_' not in guessed:
            print("You won!!")
            break






# word = 'evaporate'
# chance = 6
# correct_index = []
# display = ""
# while chance < 7:
#
#     user_input = input("Guess a letter")
#     if user_input not in word:
#         chance = chance - 1
#     else:
#
#         for letters in word:
#             if user_input == letters:
#                 correct_index.append(letters)
#                 for match in range(0, len(word)):
#                     if match == correct_index:
#                         display = display + word[match]
#                     else:
#                         display = display + "_"
#                 print(display)
