import fibo

a = fibo.fib(1000)
print(a)

b = fibo.fib2(100)
print(b)

# if you want to use a function 
# Assign imported module to a local name. 

local_name = fibo.fib
a = local_name(500)
print(a)