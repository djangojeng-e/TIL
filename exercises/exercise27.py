number_list = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        i = str(i)
        number_list.append(i)

# print(number_list)

x = ','.join(number_list)
print(x)
