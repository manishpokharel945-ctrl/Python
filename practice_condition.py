# Student Grade Checker Program

print("       Student Grade Checker       ")

# Taking student details
student_name = input("Enter student name: ")
subject = input("Enter subject name: ")

# Taking marks input
marks = int(input("Enter marks out of 100: "))

print("\n---------- Result ----------")
print("Student Name:", student_name)
print("Subject:", subject)
print("Marks:", marks)

# Checking grade using if, elif, else
if marks >= 90 and marks <= 100:
    print("Grade: A+")
    print("Remarks: Excellent performance!")
elif marks >= 80 and marks < 90:
    print("Grade: A")
    print("Remarks: Very good work!")
elif marks >= 70 and marks < 80:
    print("Grade: B+")
    print("Remarks: Good performance.")
elif marks >= 60 and marks < 70:
    print("Grade: B")
    print("Remarks: Satisfactory.")
elif marks >= 50 and marks < 60:
    print("Grade: C")
    print("Remarks: Need more practice.")
elif marks >= 40 and marks < 50:
    print("Grade: D")
    print("Remarks: Passed, but improvement is needed.")
elif marks >= 0 and marks < 40:
    print("Grade: Fail")
    print("Remarks: Work harder and try again.")
else:
    print("Invalid marks! Please enter marks between 0 and 100.")

print("----------------------------")
print("Thank you for using the Grade Checker Program.")