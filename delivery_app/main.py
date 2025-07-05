import uuid
from delivery_utils import save_packages, load_packages

class Package:
    def __init__(self, sender, recipient, id=None, status="In Transit"):
        self.id = id if id else str(uuid.uuid4())  # Generate unique ID
        self.sender = sender
        self.recipient = recipient
        self.status = status

    def __str__(self):
        return f"ID: {self.id}\nSender: {self.sender}\nRecipient: {self.recipient}\nStatus: {self.status}\n"

class DeliverySystem:
    def __init__(self):
        self.packages = load_packages()

    def register_package(self):
        sender = input("Enter sender name: ")
        recipient = input("Enter recipient name: ")
        new_package = Package(sender, recipient)
        self.packages.append(new_package)
        print("Package registered successfully!")

    def mark_as_delivered(self):
        package_id = input("Enter package ID: ")
        for pkg in self.packages:
            if pkg.id == package_id:
                pkg.status = "Delivered"
                print("Package marked as delivered.")
                return
        print("Package not found.")

    def view_packages(self):
        if not self.packages:
            print("No packages registered.")
        for pkg in self.packages:
            print(pkg)

    def save_and_exit(self):
        save_packages(self.packages)
        print("Data saved. Goodbye!")

def main():
    system = DeliverySystem()

    while True:
        print("\n--- PACKAGE DELIVERY SYSTEM ---")
        print("1. Register a package")
        print("2. Mark package as delivered")
        print("3. View all packages")
        print("4. Save & Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            system.register_package()
        elif choice == "2":
            system.mark_as_delivered()
        elif choice == "3":
            system.view_packages()
        elif choice == "4":
            system.save_and_exit()
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()