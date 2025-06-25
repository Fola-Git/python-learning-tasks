# List to store expenses
expenses = []

# Function to add a new expense
def add_expense():
    try:
        item = input("Enter item description: ").strip()
        amount = float(input("Enter amount: "))
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        expenses.append({"item": item, "amount": amount})
        print("Expense added successfully.\n")
    except ValueError as ve:
        print(f"Error: {ve}\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("--- All Expenses ---")
    for expense in expenses:
        print(f"{expense['item']} - ${expense['amount']:.2f}")
    print()

# Function to show total and average expenses
def total_and_average():
    if not expenses:
        print("No expenses to calculate.\n")
        return
    total = sum(exp['amount'] for exp in expenses)
    average = total / len(expenses)
    print(f"Total Expenses: ${total:.2f}")
    print(f"Average Expense: ${average:.2f}\n")

# Menu for user interaction
def menu():
    print("Welcome to Expense Tracker")
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total and Average")
        print("4. Exit\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_and_average()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()