li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

li = set(li)    # Use set method to convert a list into a set

print(li)
li = list(li)
# Use list method to convert a set back into a list.
# This way, the duplicate values are removed.
print(li)


# Suggested Solution

def removeDuplicate(li):
    newli = []
    seen = set()
    for item in li:
        if item not in seen:
            seen.add(item)
            newli.append(item)
    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))