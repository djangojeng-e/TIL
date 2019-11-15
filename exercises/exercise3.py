
#1 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for a in a:
    if a < 5:
        new_list.append(a)

print(new_list)

#2 Use list comprehension 
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
comprehensive_list = [b for b in b if b < 5]

# print(comprehensive_list)

#3 
c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_number = int(input("Please enter your number: "))
user_list = []
for c in c:
    if c < user_number: 
        user_list.append(c)

print(user_list)



