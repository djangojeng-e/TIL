import re

string = '2 cats and 3 dogs'

pattern = "\d+"

numbers = re.findall(pattern, string)
print(numbers)

# re.findall(pattern, string, flags=0)
# Return all non-overlapping matches of pattern in string,
# as a list of string
# The string is scanned left-to-right, and matches are returned in the other found.
# If one or more groups are present in the pattern, return a list of groups.
# This will be a list of tuples if the pattern has more than one group.
# Empty matches are included in the result.



