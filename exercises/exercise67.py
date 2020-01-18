
def my_tuple(n1, n2):
    my_tuple = [x for x in range(n1, n2)]
    return my_tuple

tup = my_tuple(1,11)
tup = list(tup)
new_list = []

for items in tup:
    if items % 2 == 0:
        new_list.append(items)

new_list = tuple(new_list)

print(new_list)





