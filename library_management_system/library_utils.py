import json
import os

DATA_FILE = "library_data.json"

def save_books(books):
    data = [{'title': b.title, 'author': b.author, 'available': b.available} for b in books]
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        return [Book(**book) for book in data]

from main import Book
