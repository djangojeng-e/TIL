
n = int(input("Please enter a number"))
float_list = []
for i in range(1, n+1):
    float_number = i / (i+1)
    float_list.append(float_number)

total = 0
for j in float_list:
    total = total + j

total = float(total)
total = round(total, 2)

print(total)