string_one = input("Please enter the first string.")
string_two = input("Please enter the second string.")


def maximum_length(s1, s2):
    if len(s1) == len(s2):
        for s in s1:
            print(s)
        for s in s2:
            print(s)
    elif len(s1) > len(s2):
        print(s1)
    else:
        print(s2)

maximum_length(string_one, string_two)


