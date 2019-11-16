user_number = int(input("Please enter your number : "))

divisor = []

for i in range(1,user_number):
    if user_number % i == 0: 
        divisor.append(i)

print(divisor)
