import json
import os

DIARY_FILE = "diary_data.json"

def save_entries(entries):
    data = [vars(entry) for entry in entries]
    with open(DIARY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_entries():
    if not os.path.exists(DIARY_FILE):
        return []
    with open(DIARY_FILE, "r") as f:
        data = json.load(f)
        from main import DiaryEntry
        return [DiaryEntry(**d) for d in data]