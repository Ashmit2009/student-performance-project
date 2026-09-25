from student_management import student_management
from marks_manager import marks_management
from grade_calculator import grade_calculator
from performane_analysis import performance_analysis

while True:

 print()
 print("*** STUDENT PERFORMANCE SYSTEM ***")

 print("1. Student Management")
 print("2. Marks Management")
 print("3. Grade Management")
 print("4. Performance Analysis")
 print("5. Exit")

 choice = input("Enter your choice: ")

 if choice == "1":
    student_management()

 elif choice == "2":
    marks_management()

 elif choice == "3":
    grade_calculator()

 elif choice == "4":
    performance_analysis()

 elif choice == "5":
    print("Exit")

 else:
    print("Thank you.") 