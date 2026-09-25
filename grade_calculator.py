def grade_calculator():

    python = float(input("Enter Python marks: "))
    calculus = float(input("Enter Calculus marks: "))
    english = float(input("Enter English marks: "))
    chy = float(input("Enter CHY marks: "))

    total = python + calculus + english + chy
    percentage = (total / 400) * 100

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

    input("Thank you")
