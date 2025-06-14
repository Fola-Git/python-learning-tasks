"""
Task 5: Simple ATM Simulator

Scenario:
Simulate a basic ATM system that allows a user to perform multiple banking operations.

Instructions:
- Start with a fixed account balance (e.g., $1,000).
- Show a menu in a loop:
    1. Check Balance
    2. Deposit
    3. Withdraw
    4. Exit
- For each choice:
    - If 1: Show current balance.
    - If 2: Ask how much to deposit, add to balance.
    - If 3: Ask how much to withdraw.
        - If amount > balance, show error.
        - Else, subtract from balance.
    - If 4: Exit the loop.
- After exit, display a goodbye message with the final balance.
"""
balance = 250000

print("Welcome to the Starr's ATM Machine!")

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Your balance is: $" + str(balance))
    elif choice == "2":
        deposit_input = input("Enter amount to deposit: ")
        deposit = int(deposit_input)
        if deposit > 0:
            balance += deposit
            print("Deposit successful.")
        else:
            print("Invalid amount.")
    elif choice == "3":
        withdraw_input = input("Enter amount to withdraw: ")
        withdraw = int(withdraw_input)
        if withdraw > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw
            print("Withdrawal successful.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")

print("\nThank you for using the ATM. Your Current balance is: $" + str(balance))
