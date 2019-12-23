user_number = int(input("Please enter the end number of your list : "))
user_list = [x for x in range(1, user_number+1)]

odd_number_list = [odd for odd in user_list if odd % 2 != 0]

square_number_list = [number ** 2 for number in odd_number_list]

print(square_number_list)