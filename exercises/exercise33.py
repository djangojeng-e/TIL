
x = int(input("Please enter the first digit"))
y = int(input("Please enter the second digit"))

output_list = []

while len(output_list) < x - 1:
    for i in range(0, x):
        list_2d = []
        output_list.append(list_2d)
        for j in range(0 ,y):
            number = i * j
            output_list[i].append(number)


print(output_list)