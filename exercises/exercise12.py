
def list_ends(list_1):
    new_list = []      
# Creates an empty list to contain the first and last elements of the list input

    new_list.append(list_1[0]) 
    # Adding the first element of list input in new_list
    new_list.append(list_1[-1])
    # Adding the last element of list input in new_list 

    print(new_list) 


a = [5, 10, 15, 20, 25]
list_ends(a) 

