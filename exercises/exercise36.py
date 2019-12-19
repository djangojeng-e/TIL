
user_input = input("Please enter your words")
words = user_input.split()

print(words)

words = set(words)          # Make words to set to remove the duplicates.
words = list(words)         # Redefine set back to the list after removal of duplicates.

words = sorted(words)       # sorts the list alphabetically

print(" ".join(words))


