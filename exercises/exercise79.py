import re

email_address = "john@citizen.com"

pattern = "(\w+)@((\w+\.)+(com))"

# \w matches any alphanumeric character and the underscore.
# \w equivalent to [a-zA-Z0-9_]
# \. decimal point character

return_string = re.match(pattern, email_address)

print(return_string)
print(return_string.group(1))
print(return_string.group(2))
print(return_string.group(3))
print(return_string.group(4))