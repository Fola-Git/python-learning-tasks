from datetime import datetime
from diary_tools import save_entries, load_entries

class DiaryEntry:
    def __init__(self, title, content, date=None):
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.title = title
        self.content = content

    def __str__(self):
        return f"Date: {self.date}\nTitle: {self.title}\nContent: {self.content}\n"

class Diary:
    def __init__(self):
        self.entries = load_entries()

    def add_entry(self):
        title = input("Entry Title: ")
        content = input("What's on your mind?\n> ")
        entry = DiaryEntry(title, content)
        self.entries.append(entry)
        print("Entry added!")

    def view_entries(self):
        if not self.entries:
            print("No entries yet.")
            return
        for entry in self.entries:
            print(entry)

    def search_entries(self):
        keyword = input("Enter date or title to search: ").lower()
        found = False
        for entry in self.entries:
            if keyword in entry.title.lower() or keyword in entry.date:
                print(entry)
                found = True
        if not found:
            print("No matching entries found.")

    def save_and_exit(self):
        save_entries(self.entries)
        print("Diary saved. Goodbye!")

def main():
    diary = Diary()
    while True:
        print("\n--- PERSONAL DIARY APP ---")
        print("1. Add entry")
        print("2. View all entries")
        print("3. Search by date or title")
        print("4. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            diary.add_entry()
        elif choice == "2":
            diary.view_entries()
        elif choice == "3":
            diary.search_entries()
        elif choice == "4":
            diary.save_and_exit()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
