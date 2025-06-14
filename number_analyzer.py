"""
Task 4: Number Analyzer

Scenario:
Build a tool to analyze numbers entered by the user.

Instructions:
- Let the user enter up to 5 numbers.
- For each number:
    - Check if it's even or odd.
    - Check if it's positive, negative, or zero.
    - Print the result for each.
- After all entries, show how many were:
    - Even
    - Odd
    - Negative
    - Zero
"""
even_count = 0
odd_count = 0
negative_count = 0
zero_count = 0

print("Enter up to 5 numbers.\n")

for i in range(5):
    number_input = input("Enter a number: ")
    number = int(number_input)

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if number < 0:
        negative_count += 1
    elif number == 0:
        zero_count += 1

print("\nResults:")
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Negative numbers:", negative_count)
print("0s:", zero_count)
