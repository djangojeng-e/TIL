user_string = input("Please enter a sentence.")

string_list = user_string.split(' ')
print(string_list)
reversed_string = string_list[-1::-1]
result = " ".join(reversed_string)
print(result)



