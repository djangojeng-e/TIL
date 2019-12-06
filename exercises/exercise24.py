# List = open(".txt").readlines()
# print(List)

lines_list = open('.txt').read().splitlines()
# Making the lines in file into the list

lines_list2 = lines_list
# Copying the original list to check against later.

lines_list = set(lines_list)    # Removing duplicated items from list
lines_list = list(lines_list)   # Removing duplicated items from list

# Count how many times the names are there and print them.

for i in lines_list:
    count = lines_list2.count(i)
    print(f'{i} is in list {count} times')
