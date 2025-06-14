"""
Task 3: Amusement Park Entry Checker

Scenario:
Check multiple visitors' ticket prices.

Instructions:
- Use a loop to allow repeated entries.
- For each visitor:
  - Ask name and age.
  - Based on age:
      < 5: Free
      5-17: $5
      18-59: $10
      60+: $7
  - Ask if they have a coupon (Yes/No). If yes, apply 20% discount.
  - Show final price.
- Exit loop when a special name like 'done' is entered.
"""
print("Welcome to the Amusement Park!")
print("Type 'done' when you're finished.\n")

while True:
    name = input("Enter visitor's name: ")
    if name.lower() == "done":
        break

    age_input = input("Enter visitor's age: ")
    age = int(age_input)

    if age < 5:
        price = 0
    elif age >= 5 and age <= 17:
        price = 5
    elif age >= 18 and age <= 59:
        price = 10
    else:
        price = 7

    coupon = input("Do you have a coupon? (Yes/No): ")
    if coupon.lower() == "yes":
        discount = price * 0.2
        price = price - discount

    print("Final price for", name + ":", "$" + str(round(price, 2)) + "\n")
