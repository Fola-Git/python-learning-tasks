"""
Task 2: Fast Food Order System

Scenario:
A fast-food ordering system that supports multiple customers.

Instructions:
- Use a loop to serve multiple customers (stop when user types 'exit').
- For each customer:
  - Ask for name and quantity of: Burger ($5), Fries ($2), Drink ($1.5)
  - Calculate total.
  - If total > $20, apply 10% discount.
  - Display the bill.
- After exit, show how many customers were served.
"""
burger_price = 5
fries_price = 2
drink_price = 1.5

customer_count = 0

print("Welcome to My First Code - Fast Food Order System!")
print("You can type 'exit' anytime to stop ordering.\n")

while True:
    customer_name = input("Enter your name: ")

    if customer_name.lower() == "exit":
        break

    burger_input = input("How many burgers would you like? ")
    if burger_input.lower() == "exit":
        break
    burger_qty = int(burger_input)

    fries_input = input("How many fries would you like? ")
    if fries_input.lower() == "exit":
        break
    fries_qty = int(fries_input)

    drink_input = input("How many drinks would you like? ")
    if drink_input.lower() == "exit":
        break
    drink_qty = int(drink_input)

    total = (burger_qty * burger_price) + (fries_qty * fries_price) + (drink_qty * drink_price)

    if total > 20:
        discount = total * 0.10
        total -= discount
        print("You got a 10% discount!")

    print("Order for:", customer_name)
    print("Total Bill: $" + str(round(total, 2)) + "\n")

    customer_count += 1

print("\nAll orders completed!")
print("Total customers served: " + str(customer_count))
