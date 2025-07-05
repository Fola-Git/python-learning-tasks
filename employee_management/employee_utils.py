import json
import os

EMPLOYEE_FILE = "employees.json"

def save_employees(employees):
    data = [vars(emp) for emp in employees]
    with open(EMPLOYEE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_employees():
    if not os.path.exists(EMPLOYEE_FILE):
        return []
    with open(EMPLOYEE_FILE, "r") as f:
        from main import Employee
        return [Employee(**emp) for emp in json.load(f)]
