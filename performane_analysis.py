def performance_analysis():
    
    class_total = 0
    num_students = int(input("Enter number of students: "))

    if num_students > 0:
        for i in range(num_students):
            print("\nStudent", i + 1)
            python = float(input("Enter Python marks: "))
            calculus = float(input("Enter Calculus marks: "))
            english = float(input("Enter English marks: "))
            chy = float(input("Enter CHY marks: "))

            total_marks = python + calculus + english + chy
            percentage = (total_marks / 400) * 100

            class_total = class_total + percentage

        avg = class_total / num_students

        print("\n*** Performance Analysis ***")
        print("Class Average Percentage:", avg, "%")
    else:
        print("No students entered.")