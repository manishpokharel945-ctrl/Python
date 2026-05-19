marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Excellent!")
    print("Your grade is A+")
elif marks >= 80:
    print("Very good!")
    print("Your grade is A")
elif marks >= 70:
    print("Good job!")
    print("Your grade is B")
elif marks >= 60:
    print("You passed.")
    print("Your grade is C")
elif marks >= 40:
    print("You just passed.")
    print("Your grade is D")
else:
    print("You failed.")
    print("You need to study harder.")