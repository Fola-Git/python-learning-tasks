# List to store history
history = []

# Function for addition
def add(x, y):
    result = x + y
    history.append(f"{x} + {y} = {result}")
    print(f"Result: {result}\n")

# Function for subtraction
def subtract(x, y):
    result = x - y
    history.append(f"{x} - {y} = {result}")
    print(f"Result: {result}\n")

# Function for multiplication
def multiply(x, y):
    result = x * y
    history.append(f"{x} * {y} = {result}")
    print(f"Result: {result}\n")

# Function for division with error handling
def divide(x, y):
    try:
        result = x / y
        history.append(f"{x} / {y} = {result}")
        print(f"Result: {result}\n")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.\n")

# Function to display history
def view_history():
    if not history:
        print("No history available.\n")
        return
    print("--- Calculation History ---")
    for i, record in enumerate(history, start=1):
        print(f"{i}. {record}")
    print()

# Function to get two numbers with error handling
def get_numbers():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        return x, y
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")
        return None, None

# Menu function
def menu():
    while True:
        print("Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        print()

        if choice in ["1", "2", "3", "4"]:
            x, y = get_numbers()
            if x is None or y is None:
                continue

            if choice == "1":
                add(x, y)
            elif choice == "2":
                subtract(x, y)
            elif choice == "3":
                multiply(x, y)
            elif choice == "4":
                divide(x, y)

        elif choice == "5":
            view_history()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select between 1 and 6.\n")

# Start the program
menu()
