import re

passwords = [x for x in input("Enter your password").split(',')]

for password in passwords:
    if len(password) < 6 or len(password) > 12:
        print('You have entered an invalid password.')
    else:
        if not re.search('[a-z]', password):
            continue  # Check if password contains at least 1 letter between [A-Z].
        elif not re.search('[0-9]', password):
            continue  # Check if password contains at least 1 number between [0-9].
        elif not re.search('[A-Z]', password):
            continue
        elif not re.search('[$#@]', password):  # Check if password contains at least 1 character from $#@
            continue
        else:
            print(f'(You enetered a valid password {password})')