
birthday_dictionary = {
    "Albert Einstein" : "1/12/1912",
    "Jeong Eun Kim" : "21/12/1983",
    "Djangojeng-e" : "18/12/1986",
    "Django": "01/01/2005"
}


name = input("Who's Birthday do you want to look up?")

if name in birthday_dictionary: 
    print(f'{name}s birthday is {birthday_dictionary[name]}') 
else: 
    print("We dont' have {}'s birthday".format(name))


