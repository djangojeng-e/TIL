user1_input = int(input("Please enter number 1 : Rock or 2 : Scissors or 3 : Papers.")) 
user2_input = int(input("Please enter number 1 : Rock or 2 : Scissors or 3 : Papers."))

if user1_input == 1:
    user1_input = 'Rock'
elif user1_input == 2:
    user1_input = 'Scissors'
else:
    user1_input = 'Papers' 

if user2_input == 1:
    user2_input = 'Rock' 
elif user2_input == 2:
    user2_input = 'Scissors'
else:
    user2_input = 'Papers' 

while user1_input != user2_input:
    if user1_input == 'Rock': 
        if user2_input == 'Papers':
            print("User2 is the winner") 
            break 
        elif user2_input == 'Scissors': 
            print("User1 is the winner")
            break 
    elif user1_input == 'Scissors': 
        if user2_input == 'Rock':
            print("User2 is the winner.")
            break
        elif user2_input == 'Papers': 
            print("User1 is the winner.")
            break
    elif user1_input == 'Papers': 
        if user2_input == 'Scissors':
            print("User2 is the winner.") 
            break 
        elif user2_input == 'Rock':
            print("User1 is the winner.") 
            break 



