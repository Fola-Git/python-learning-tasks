import json
import math
from datetime import datetime
import os

BILL_FILE = "bills.json"

def save_bill(cart):
    bill_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "products": [vars(p) for p in cart.products],
        "total": cart.calculate_total()
    }

    history = load_bills()
    history.append(bill_data)

    with open(BILL_FILE, "w") as f:
        json.dump(history, f, indent=4)

def load_bills():
    if not os.path.exists(BILL_FILE):
        return []
    with open(BILL_FILE, "r") as f:
        return json.load(f)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append(Product(name, price, quantity))

    def calculate_total(self):
        total = sum(p.price * p.quantity for p in self.products)
        if total > 10000:
            print("Discount applied: 10%")
            total *= 0.90  # 10% discount
        return math.ceil(total)

    def view_cart(self):
        if not self.products:
            print("Cart is empty.")
            return
        for p in self.products:
            print(f"{p.name} - ₦{p.price} x {p.quantity}")
        print(f"Total: ₦{self.calculate_total()}")
