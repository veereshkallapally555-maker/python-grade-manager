# Student Grade Checker

school_name = "ABC School"
pass_mark = 35
is_exam_active = True

print(f"Welcome to {school_name}")
print(f"Exam Active: {is_exam_active}")

# Get valid number of students
while True:
    try:
        num_students = int(input("Enter number of students: "))

        if num_students <= 0:
            print("❌ Number of students must be greater than 0.")
            continue

        break

    except ValueError:
        print("❌ Please enter a valid number.")


total_marks = 0.0
passed_students = 0

for i in range(num_students):
    print(f"\nStudent {i + 1}")

    # Get valid student name
    while True:
        name = input("Enter student name: ").strip()

        if name:
            break

        print("❌ Student name cannot be empty.")

    # Get valid marks
    while True:
        try:
            marks = float(input("Enter marks: "))

            if 0 <= marks <= 100:
                break

            print("❌ Marks must be between 0 and 100.")

        except ValueError:
            print("❌ Please enter a valid number.")

    total_marks += marks

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= pass_mark:
        grade = "D"
    else:
        grade = "F"

    passed = marks >= pass_mark

    if passed:
        passed_students += 1

    print(f"{name} scored {marks} and got grade {grade}")
    print(f"Passed: {passed}")


average = total_marks / num_students

print("\n===== SUMMARY =====")
print(f"Total Students : {num_students}")
print(f"Passed Students: {passed_students}")
print(f"Average Marks  : {average:.2f}")


choice = "yes"

while choice.lower() == "yes":
    print("\nThank you for using the Grade Checker!")
    choice = input("Type 'no' to exit: ")

print("Program ended.")


# *args example
def calculate_total(*args):
    total = 0

    for num in args:
        total += num

    return total


print("Total:", calculate_total(10, 20, 30))
