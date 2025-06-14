# Ask how many students to evaluate
number_of_students = int(input("How many students do you want to process? "))

# Initialize counters for summary
total_passed = 0
total_failed = 0
total_excellent = 0

# Loop through each student
for student_number in range(number_of_students):
    print(f"\n--- Processing Student {student_number + 1} ---")

    # Get student's name
    student_name = input("Enter the student's name: ")

    # Collect 3 subject scores
    subject_scores = []

    for subject_index in range(1, 4):
        # Ask for the score for each subject
        score = float(input(f"Enter score for Subject {subject_index}: "))
        subject_scores.append(score)

    # Calculate the average of the 3 scores
    average_score = sum(subject_scores) / 3

    # Print student's average
    print(f"{student_name}'s average score is: {average_score:.2f}")

    # Check performance based on average
    if average_score < 50:
        print("Result: Fail")
        total_failed += 1
    elif 50 <= average_score < 80:
        print("Result: Pass")
        total_passed += 1
    else:
        print("Result: Excellent!")
        total_excellent += 1

# Print summary after all students are processed
print(f"Total Passed: {total_passed}")
print(f"Total Failed: {total_failed}")
print(f"Total Excellent: {total_excellent}")