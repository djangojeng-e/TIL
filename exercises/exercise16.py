import random 

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"
passlength = 8 

p = "".join(random.sample(s, passlength))
print(p)