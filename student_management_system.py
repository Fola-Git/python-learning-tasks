# This will show list to store student information
students = []

# Function to add a new student
def add_student():
    try:
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        scores = []
        for i in range(1, 4):
            score = float(input(f"Enter score for subject {i}: "))
            if score < 0 or score > 100:
                raise ValueError("Score must be between 0 and 100.")
            scores.append(score)

        student = {
            "name": name,
            "scores": scores
        }
        students.append(student)
        print(f"{name} has been added successfully.\n")

    except ValueError as ve:
        print(f"Error: {ve}\n")

# Function to calculate average score
def calculate_average(scores):
    return sum(scores) / len(scores)

# Function to determine performance status
def get_performance(average):
    if average >= 70:
        return "Excellent"
    elif average >= 50:
        return "Good"
    else:
        return "Needs Improvement"

# Function to display all students
def show_all_students():
    if not students:
        print("No students in the list.\n")
        return

    print("List of Students:")
    for student in students:
        avg = calculate_average(student["scores"])
        status = get_performance(avg)
        print(f"Name: {student['name']}, Scores: {student['scores']}, Average: {avg:.2f}, Status: {status}")
    print()

# Function to search for a student by name
def search_student():
    name = input("Enter student name to search: ").strip()
    found = False
    for student in students:
        if student["name"].lower() == name.lower():
            avg = calculate_average(student["scores"])
            status = get_performance(avg)
            print(f"Student found:")
            print(f"Name: {student['name']}, Scores: {student['scores']}, Average: {avg:.2f}, Status: {status}\n")
            found = True
            break
    if not found:
        print("Student not found.\n")

# Menu to display options
def menu():
    while True:
        print("Student Management System")
        print("1. Add New Student")
        print("2. Show All Students")
        print("3. Search Student by Name")
        print("4. Exit")

        try:
            choice = int(input("Choose an option (1-4): "))
            print()
            if choice == 1:
                add_student()
            elif choice == 2:
                show_all_students()
            elif choice == 3:
                search_student()
            elif choice == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

# This will run the program
menu()
