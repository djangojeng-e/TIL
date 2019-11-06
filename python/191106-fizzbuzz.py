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

# operator with bool -> It can be 0 or 1. 
# for i in range(1,100+1):
#   if i%3==0 or i%5==0: 
#    print("fizz"*(i%3==0) + "buzz"*(i%5==0)
    #else: 
        #print(i)


# Fizzbuzz in List comprehension

# ["fizz buzz" if i%15==0 else "fizz" if i%3==0 else "buzz" if i%5==0 else i for i in range(0,101)]



