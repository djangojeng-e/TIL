# Fizzbuzz.py 
# multiples of 3 = print "fizz"
# multiples of 5 = print "buzz"
#

for i in range(1,101): 
    if i % 3 == 0:
        print("Fizz") 
    elif i % 5 == 0: 
        print("Buzz")
    elif i % 15 == 0: 
        print("Fizzbuzz") 
    else:
        print(i)


# for i in range(1,100+1):
#   if i%3==0 or i%5==0: 
#    print("fizz"*(i%3==0) + "buzz"*(i%5==0)
    #else: 
        #print(i)


