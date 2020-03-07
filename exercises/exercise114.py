# A closure in Python is said to occur
# when a nested function references
# a value in its enclosing scope.
# The whole point here is that it remembers the value

def A(x):
    def B():
        print(x)
    return B

A(7)()
