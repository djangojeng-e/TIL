string = "abcdefgabc"
string_list = []
for letter in string:
    string_list.append(letter)

print(string_list)

string_list_no_duplicate = set(string_list)
string_list_no_duplicate = list(string_list_no_duplicate)

string_list_no_duplicate.sort()
print(string_list_no_duplicate)

for letters in string_list_no_duplicate:
    string_count = string_list.count(letters)
    print(f'{letters}, {string_count}')


# Suggested Solution

# dict = {}
# for s in string:
#     dict[s] = dict.get(s,0)+1
#
# print('\n'.join.[f'{k}, {v}' for k, v in dict.items()])
#




