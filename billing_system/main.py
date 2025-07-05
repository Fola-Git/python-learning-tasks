from billing import Cart, save_bill, load_bills

def main():
    cart = Cart()

    while True:
        print("\n--- STARR'S SHOP BILLING SYSTEM ---")
        print("1. Add product to cart")
        print("2. View cart and total")
        print("3. Save bill")
        print("4. View previous transactions")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            name = input("Product name: ")
            try:
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                cart.add_product(name, price, quantity)
                print("Product added.")
            except ValueError:
                print("Invalid input. Price must be a number.")
        elif choice == "2":
            cart.view_cart()
        elif choice == "3":
            save_bill(cart)
            print("Bill saved.")
        elif choice == "4":
            history = load_bills()
            if not history:
                print("No previous bills.")
            else:
                for bill in history:
                    print(f"\nDate: {bill['timestamp']}")
                    for p in bill["products"]:
                        print(f"{p['name']} - ₦{p['price']} x {p['quantity']}")
                    print(f"Total: ₦{bill['total']}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
