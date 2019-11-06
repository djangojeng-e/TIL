
# fizzbuzz exercise 
# for the numbers between 0 to 100, print "fizz" if the number 
# is divisible by 3 and print "buzz" if the number is divisible by 5
# if the number is divisible by 15, print the whole word "fizzbuzz". 

# 1. execute the above using 1 loop statement with conditional statements  
# 2. execute the above using 1 loop statement with one conditional statement 
# 3. create the list containing the result by exploiting list comprehesion method. 


for i in range(0, 101): 
    if i % 15 == 0: 
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")


# 2 

for i in range(0, 101):
    if i % 3 == 0 or i % 5 == 0: 
        print("fizz"*(i % 3 == 0) + "buzz"*(i % 5 == 0))
    else:
        print(i)
