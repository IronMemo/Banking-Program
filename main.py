balance = 0
withdraw_history = []

def menu():
    print("[1] Show Balance ")
    print("[2] Deposit ")
    print("[3] Withdraw ")
    print("[4] Show Withdraw History")
    print("[5] Exit ")

menu()
option = int(input("Enter your option: "))

while option != 5:
    if option == 1:
        print(f"Your current balance is: ${balance}")
    elif option == 2:
        deposit = float(input("Enter the amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print(f"${deposit} has been added to your account.")
        else:
            print("Invalid amount. Please enter a positive value.")
    elif option == 3:
        withdraw = float(input("Enter the amount you want to withdraw: "))
        if withdraw > 0 and withdraw <= balance:
            balance -= withdraw
            print(f"${withdraw} has been withdrawn from your account.")
            withdraw_history.append(f"Withdrew ${withdraw:.2f}")
        elif withdraw > balance:
            print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive value.")
    elif option == 4:
        if len(withdraw_history) == 0:
            print("No withdrawals have been made yet.")
        else:
            print("Withdraw History:")
            for transaction in withdraw_history:
                print(transaction)
    else:
        print("Invalid option. Please select a valid menu option.")

    print()
    menu()
    option = int(input("Enter your option: "))

print("Thank you for using the banking system!")
