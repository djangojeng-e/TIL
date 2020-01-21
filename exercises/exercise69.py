the_list = [1,2,3,4,5,6,7,8,9,10]


def filter_evens(li):
   even_numbers = [items for items in the_list if items % 2 ==0]
   print(even_numbers)


filter_evens(the_list)