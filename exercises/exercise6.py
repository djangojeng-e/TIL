def previous_solution():

    string = input("Enter your string")

    string_reverse = string[-1::-1]

    if string_reverse == string:
        print("Your string is a Palindrome.")
    else:
        print("Your string is not a Palindrome.")


# Another solution on 08/02/2020 starts here.

string = input('enter your string  ')

reverse_string = string[-1::-1]

if reverse_string == string:
    print('It is a pallindrome')
else:
    print('It is NOT a pallindrome')
