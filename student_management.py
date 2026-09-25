students_list = []

def student_management():
 while True:
    print()
    print("\n*** STUDENT MANAGEMENT ***")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        id = input("Enter ID: ")
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        student = {"id": id, "name": name, "branch": branch, "year": year}
        students_list.append(student)
        print("Student added successfully.")

    elif choice == "2":
        if len(students_list) == 0:
            print("List is empty")
        else:
            print("\n*** All Students ***")
            for student in students_list:
                print("id:", student["id"]), 
                print("name:", student["name"]), 
                print("branch:", student["branch"]), 
                print("year:", student["year"])

    elif choice == "3":
        search_id = input("Enter Student ID to search: ")
        found = False
        for student in students_list:
            if student["id"] == search_id:
                print("Student found:")
                print("id:", student["id"]), 
                print("name:", student["name"]), 
                print("branch:", student["branch"]), 
                print("year:", student["year"])
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        update_id = input("Enter Student ID to update: ")
        found = False
        for student in students_list:
            if student["id"] == update_id:
                print("Student found. Enter new details:")
                student["name"] = input("Enter Student Name: ")
                student["branch"] = input("Enter Branch: ")
                student["year"] = input("Enter Year: ")
                print("Student updated successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        delete_id = input("Enter Student ID to delete: ")
        found = False
        for student in students_list:
            if student["id"] == delete_id:
                students_list.remove(student)
                print("Student deleted successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Thank you.")

     

    
            



                
            

            
         
           
           