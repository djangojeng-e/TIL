user_number = input("Please enter your digit : ")

total = 0
for i in range(1, 5):
    number = user_number * i
    total = total + int(number)

print(total)