from library_utils import save_books, load_books

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    def __init__(self):
        self.books = load_books()

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.available:
                book.available = False
                print(f"You borrowed '{book.title}'.")
                return
        print("Book not available or doesn't exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.available:
                book.available = True
                print(f"You returned '{book.title}'.")
                return
        print("This book was not borrowed or doesn't exist.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def save_and_exit(self):
        save_books(self.books)
        print("Library saved. Goodbye!")

def main():
    lib = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View all books")
        print("5. Save & Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            lib.add_book(title, author)

        elif choice == '2':
            title = input("Enter title to borrow: ")
            lib.borrow_book(title)

        elif choice == '3':
            title = input("Enter title to return: ")
            lib.return_book(title)

        elif choice == '4':
            lib.view_books()

        elif choice == '5':
            lib.save_and_exit()
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
