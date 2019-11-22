
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if len(a) < len(b): 
    c = [a for a in a if a in b]    # Use of List comprehension.
else: 
    c = [b for b in b if b in a] 


print(c)


# Refer to the solution below for the original answer. 

#c = [] 

# Create List c  contains only the elements that are common between the list.

#for a in a: 
#    if a in b: 
#        c.append(a) 
#    else: 
#        continue

#print(c)

