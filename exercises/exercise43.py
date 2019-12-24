balance = 0

while True:
    print("Please select your action")
    print("Press 1 to put deposit amount")
    print("Press 2 to withdraw amount")
    print("Press 0 to exit")
    user_input = int(input("Please enter your input command : "))
    if user_input == 0:
        break
    elif user_input == 1:
        deposit_amount = int(input("Please enter your deposit amount : "))
        if deposit_amount < 0:
            print("Please enter the amount greater than 0.")
        else:
            balance += deposit_amount
    elif user_input == 2:
        withdraw_amount = int(input("Please enter your withdraw amount : "))
        if withdraw_amount > balance:
            print("Insufficient funds available in your account.")
        else:
            balance -= withdraw_amount

print(balance)


