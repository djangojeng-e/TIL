# A set is a collection of items, where cannot be any duplicates.
# A set is also unordered.

myset = {1, 3, 2, 2}
print(myset)

# A set cannot be indexed.

# However, a set is mutable.
# A frozen set is immutable.

# This means, we cannot change its values. This also makes it eligible to be used
# as a key for a dictionary.

myset = frozenset([1,3,2,2])
print(myset)

print(type(myset))