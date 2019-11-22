# Understanding Instance 

# It is fairly important to understand Instances. 

# This example might help understand instances. 

list1 = [1, 2, 3] 
list2 = [1, 2, 3] 


if list1 is list1: 
    print("Of Course! list1 and list1 is the same instance!") 

if list1 == list2:
    print("list1 and list2 values are the same") 
    if list1 is list2: 
        print("And list1 and list2 are the same instance") 
    else:
        print("However, list1 and list2 are different instances.") 

print()
print()
print()
print("------"*8)
# The codes below inspect if list1 and list2 are "List Class". 


list1 = list(range(10)) 
list2 = [1 ,2, 3] 

if isinstance(list1, list) and isinstance(list2, list):
    print("List1 and List 2 are both 'List Class'.")


