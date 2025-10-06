try:
    marks = float(input("Enter marks: "))
    if marks < 0:
        print("Marks cannot be negative. Please enter a valid number.")
    elif marks >= 90 and marks < 100:
        print("Grade: O")
    elif marks >= 80:
        print("Grade: A+")
    elif marks >= 70:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B+")
    elif marks >= 50:
        print("Grade: B")
    else:
        print("Grade: F")
except ValueError:
    print("Invalid input. Please enter a valid number.")