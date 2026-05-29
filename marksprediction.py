# Student Marks Analyzer
# A simple Python project to analyze student marks

students = {}

def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100.")
    else:
        students[name] = marks
        print("Student added successfully!")

def show_results():
    if not students:
        print("No student data available.")
        return

    print("\n--- Student Results ---")

    total_marks = 0

    for name, marks in students.items():
        grade = calculate_grade(marks)
        status = "Pass" if marks >= 40 else "Fail"

        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")
        print("----------------------")

        total_marks += marks

    average = total_marks / len(students)

    highest_student = max(students, key=students.get)
    lowest_student = min(students, key=students.get)

    print("\n--- Class Summary ---")
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Scorer: {highest_student} ({students[highest_student]})")
    print(f"Lowest Scorer: {lowest_student} ({students[lowest_student]})")

while True:
    print("\n===== Student Marks Analyzer =====")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_results()
    elif choice == "3":
        print("Thank you for using Student Marks Analyzer!")
        break
    else:
        print("Invalid choice. Please try again.")