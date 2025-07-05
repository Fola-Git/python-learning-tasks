import json
import os

DATA_FILE = "delivery_data.json"

def save_packages(packages):
    # Convert package objects into dictionary format before saving
    data = [vars(p) for p in packages]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_packages():
    # If file doesn't exist, return empty list
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        from main import Package  # import here to avoid circular import
        return [Package(**p) for p in data]
