# Use of function will be the key to the solution. 


user_number = int(input("Please enter your number.")) 

for i in range(1, user_number): 
    if user_number % i !=  0:
        print("The number is  a prime number.")
        break
    else:
        continue



