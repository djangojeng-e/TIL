# user_text = input("Please enter your sentence : ")

user_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"

text = user_text.split(' ')
text = sorted(text)
print(text)

words = {}

for word in text:
    words[word] = text.count(word)


for key, value in words.items():
    print(f'{key} : {value}')



# print(words.keys())
# print(words.values())
#
#
# for word in text:
#     word_count = 0
#     word_count = text.count(word)
#     print(f'{word} : {word_count}')
#

# Solution suggested
#
# freq = {}   # frequency of words in text
# line = input("Enter your sentence : ")
# for word in line.split(' '):
#     freq[word] = freq.get(word,0) +1
#
# words = freq.keys()
# words.sort()
#
# for w in words:
#     print("%s : %d" % (w, freq[w]))

# print(text)