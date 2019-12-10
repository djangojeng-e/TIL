# Diving into Regular Expression



Getting a small bit of text out of a large block of text is quite challenging but always desired in many cases. 



In python, strings have methods to manipulate strings using the methods below. 



**index(), find(), split(), count(), replace()**



If you cannot manage to abstract or find or manipulate strings to handle special cases, **Regular Expression** is the area that you need to move up into.



Regular expressions are powerful and standardised way of searching, replacing and parsing text with complex patterns of characters. The regular expression syntax looks very tight and strange but its result can end up being more readable than hand-rolled solution that uses a long chain of string functions. 



**Regular Expressions are similar in other languages like Perl, JavaScript or PHP**





# Case Study : Street Addresses 





```python

# Example 1 

s = '100 NORTH MAIN ROAD'
s = s.replace('ROAD', 'RD.')
print(s)

# Example 2 

s = '100 NORTH BROAD ROAD'
s = s.replace('ROAD', 'RD.')
print(s)

# Example 3 

s = '100 NORTH MAIN ROAD'

s = s[:-4] + s[-4:].replace('ROAD', 'RD')
print(s)

import re 

x = re.sub('ROAD$', 'RD', s)
print(x)
```





