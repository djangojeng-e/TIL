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


# Another Solution attempted on 14/2/2020

while True:
    print("Please input your command")
    print("1 : Play Rock, Scissors and Paper Game")
    print("0 : Exit the Game\n")
    command = int(input("\nEnter your command"))

    if command == 0:
        break
    elif command == 1:
        choices = []
        for i in range(1, 3):
            plays = ['Rock', 'Scissors', 'Players']
            print(f'Enter play for user {i}\n')
            print("1. Rock \n",
                  "2. Scissors \n",
                  "3. Paper\n",)
            choice = int(input("\nPlease enter your choice"))
            if choice == 1:
                choices.append("Rock")
            if choice == 2:
                choices.append("Scissors")
            if choice == 3:
                choices.append("Paper")
        if choices[0] == choices[1]:
            print("===" * 10)
            print("It is a draw")
            print("===" * 10)
        else:
            if choices[0] == "Rock" and choices[1] == "Scissors":
                print("\nPlayer 1 is the winner\n")
            elif choices[0] == "Scissors" and choices[1] == "Paper":
                print("\nPlayer 1 is the winner\n")
            elif choices[0] == "Paper" and choices[1] == "Rock":
                print("\nPlayer1 is the winner\n")
            else:
                print("\nPlayer 2 is the winner\n")
