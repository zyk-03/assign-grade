def assign_grade():
    grade = int(input("Enter a grade: "))
    if grade > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif grade >= 90:
        print("Grade: A")
    elif grade >= 80:
        print("Grade: B")
    elif grade >= 70:
        print("Grade: C")
    elif grade >= 60:
        print("Grade: D")
    elif grade < 0:
        print("Invalid score! Please enter a value between 0 and 100.")
    else:
        print("Grade: F")
        
assign_grade()
