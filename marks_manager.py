student_marks = {}

def marks_management():
 while True:
    print("\n*** MARKS MANAGEMENT ***")
    print("1. Enter Marks")
    print("2. View Marks")
    print("3. Update Marks")
    print("4. View Result")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter ID: ")
        python = float(input("Enter Python marks: "))
        calculus = float(input("Enter Calculus marks: "))
        english = float(input("Enter English marks: "))
        chy = float(input("Enter CHY marks: "))

        student_marks[id] = [python, calculus, english, chy]
        print("Marks saved successfully!")

    elif choice == "2":
        id = input("Enter ID: ")
        if id in student_marks:
            m = student_marks[id]
            print("\n*** Student Marks ***")
            print("Python:", m[0])
            print("Calculus:", m[1])
            print("English:", m[2])
            print("CHY:", m[3])
        else:
            print("No record found.")

    elif choice  == "3":
        id = input("Enter ID to update: ")
        if id in student_marks:
            print("Enter new marks:")
            python = float(input("Enter Python marks: "))
            calculus = float(input("Enter Calculus marks: "))
            english = float(input("Enter English marks: "))
            chy = float(input("Enter CHY marks: "))
            
            student_marks[id] = [python, calculus, english, chy]
            print("Marks updated!")
        else:
            print("Student ID not found.")

    elif choice == "4":
        id = input("Enter ID to view result: ")
        if id in student_marks:
            m = student_marks[id]

            total = m[0] + m[1] + m[2] + m[3]
            percentage = total / 4

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            print("\n*** Result ***")
            print("Total Marks:", total)
            print("Percentage:", percentage, "%")
            print("Grade:", grade)
        else:
            print("Student ID not found.")

    elif choice == "5":
        print("Exit")
        break

    else:
        print("Thank you.")