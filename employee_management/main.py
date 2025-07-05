from employee_utils import save_employees, load_employees

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id} | Name: {self.name} | Dept: {self.department} | Salary: ₦{self.salary}"

class EmployeeManager:
    def __init__(self):
        self.employees = load_employees()

    def add_employee(self):
        name = input("Enter name: ")
        emp_id = input("Enter ID: ")
        department = input("Enter department: ")
        try:
            salary = float(input("Enter salary: "))
            self.employees.append(Employee(name, emp_id, department, salary))
            print("Employee added.")
        except ValueError:
            print("Invalid salary! Must be a number.")

    def view_all(self):
        if not self.employees:
            print("No employee records.")
            return
        for emp in self.employees:
            print(emp)

    def search_by_id(self):
        search_id = input("Enter employee ID to search: ")
        found = False
        for emp in self.employees:
            if emp.emp_id == search_id:
                print(emp)
                found = True
        if not found:
            print("Employee not found.")

    def save_to_file(self):
        save_employees(self.employees)
        print("Employees saved to file.")

def main():
    manager = EmployeeManager()

    while True:
        print("\n--- EMPLOYEE RECORD MANAGER ---")
        print("1. Add employee")
        print("2. View all employees")
        print("3. Search by ID")
        print("4. Save to file")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            manager.search_by_id()
        elif choice == "4":
            manager.save_to_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
