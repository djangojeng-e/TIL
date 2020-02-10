# Binary Search
# In computer science, a binary search or half-interval search algorithm finds
# the position of a target value within a sorted array.
# The binary search algorithm can be classified as a dichotomies divide and conquer search algorithm
# and executes in logarithmic time.

import math

def binary_search(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1
    return index


li = [2, 5, 7, 9, 11, 17, 222]

print(binary_search(li,11))
print(binary_search(li,12))


# refer to the link below for more understandings.
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php 