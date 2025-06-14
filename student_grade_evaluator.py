"""
Task 1: Student Grade Evaluator

Scenario: Collect and evaluate grades for multiple students

Instructions:
- Ask how many students to process.
- Use a loop to:
    - Ask for each student's name and 3 subject scores.
    - Convert scores to float, calculate the average.
    - Display result:
        - Average < 50 -> Fail
        - 50-79 -> Pass
        - 80+ -> Excellent!
- After all students are processed, display a summary:
    how many passed, failed, and got excellent
"""
number_of_students = int(input("How many students do you want to process? "))

total_passed = 0
total_failed = 0
total_excellent = 0

for student_number in range(number_of_students):
    print(f"\n--- Processing Student {student_number + 1} ---")

    student_name = input("Enter the student's name: ")

    subject_scores = []

    for subject_index in range(1, 4):
        score = float(input(f"Enter score for Subject {subject_index}: "))
        subject_scores.append(score)

    average_score = sum(subject_scores) / 3

    print(f"{student_name}'s average score is: {average_score:.2f}")

    if average_score < 50:
        print("Result: Fail")
        total_failed += 1
    elif 50 <= average_score < 80:
        print("Result: Pass")
        total_passed += 1
    else:
        print("Result: Excellent!")
        total_excellent += 1

print(f"Total Passed: {total_passed}")
print(f"Total Failed: {total_failed}")
print(f"Total Excellent: {total_excellent}")