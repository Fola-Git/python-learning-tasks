# Movie list with seat count and price
movies = {
    "Fast X": {"price": 20, "seats": 25},
    "The Little Mermaid": {"price": 15, "seats": 18},
    "Mission Impossible": {"price": 22, "seats": 12}
}

# View all movies
def view_movies():
    print("Movies Available:")
    for name, info in movies.items():
        print(f"{name}: ${info['price']} ({info['seats']} seats left)")
    print()

# Book a ticket
def book_ticket():
    movie_name = input("Enter movie name: ").strip().title()
    if movie_name not in movies:
        print("Error: Movie not found.\n")
        return

    try:
        seats_left = movies[movie_name]["seats"]
        tickets = int(input("How many tickets?: "))
        if tickets <= 0:
            print("Error: Enter a positive number.\n")
            return
        if tickets > seats_left:
            print("Error: Not enough seats available.\n")
            return

        total_cost = tickets * movies[movie_name]["price"]
        movies[movie_name]["seats"] -= tickets
        print(f"Booking successful! You paid ${total_cost}")
        print(f"{movies[movie_name]['seats']} seats remaining.\n")

    except ValueError:
        print("Error: Please enter a valid number.\n")

# Main menu
def menu():
    print("Welcome to the Movie Ticket Booking System\n")
    view_movies()  # Automatically show available movies at startup

    while True:
        print("1. Book Ticket")
        print("2. View Movies")
        print("3. Exit\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_movies()
        elif choice == "3":
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
menu()
