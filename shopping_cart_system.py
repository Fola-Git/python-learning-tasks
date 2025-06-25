# Available store items and prices
store_items = {
    "Rice": 400,
    "Beans": 350,
    "Oil": 1000,
    "Milk": 600,
    "Bread": 300
}

# Cart is a list of dictionaries
cart = []

# Function to display store items
def show_store_items():
    print("\n--- Store Items ---")
    for item, price in store_items.items():
        print(f"{item} - ₦{price}")
    print()

# Function to add an item to the cart
def add_to_cart():
    item = input("Enter item name: ").strip().title()
    if item not in store_items:
        print("Item not found in store.\n")
        return
    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        cart.append({
            "item": item,
            "quantity": quantity,
            "price": store_items[item]
        })
        print(f"{quantity} x {item} added to cart.\n")
    except ValueError as ve:
        print(f"Error: {ve}\n")

# Function to view cart contents
def view_cart():
    if not cart:
        print("Your cart is empty.\n")
        return
    print("\n--- Your Cart ---")
    for i, entry in enumerate(cart, start=1):
        name = entry['item']
        qty = entry['quantity']
        price = entry['price']
        print(f"{i}. {name} - Qty: {qty}, Unit Price: ₦{price}, Subtotal: ₦{qty * price}")
    print()

# Function to calculate total
def total_bill():
    total = sum(item['quantity'] * item['price'] for item in cart)
    print(f"Total Bill: ₦{total}\n")

# Function to remove an item from cart
def remove_item():
    item_name = input("Enter the item name to remove: ").strip().title()
    for i, item in enumerate(cart):
        if item['item'] == item_name:
            del cart[i]
            print(f"{item_name} removed from cart.\n")
            return
    print(f"{item_name} not found in cart.\n")

# Function to clear the cart
def clear_cart():
    cart.clear()
    print("Cart has been cleared.\n")

# Menu function
def menu():
    print("Welcome to Starr's Mini Store")
    while True:
        print("1. View Store Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove Item")
        print("5. Clear Cart")
        print("6. Checkout and Exit")

        choice = input("Enter your choice (1-6): ").strip()
        print()

        if choice == "1":
            show_store_items()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            clear_cart()
        elif choice == "6":
            view_cart()
            total_bill()
            print("Thank you for shopping. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.\n")

# Start the program
menu()
