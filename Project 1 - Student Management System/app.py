students=[]

while True:
    print("Press 1 to add student record: ")
    print("Press 2 to view all students record: ")
    print("Press 3 to Search student: ")
    print("Press 4 to update student record: ")
    print("Press 5 to Delete student record: ")
    print("Press 6 to Viewing student result: ")
    print("Press 7 to Exist: ")

    press=int(input("enter your choice: "))

    if press==1:
        student_id=int(input("Enter Student ID: "))
        student_name=input("Enter Student Name: ")
        student_age=int(input("Enter Student Age: "))
        student_email=input("Enter Student Email: ")
        student_Course=input("Enter Student Course: ")
        student_Semester=int(input("Enter Student Semester: "))
        student_marks=int(input("Enter Student Marks: "))

        student={
            "ID":student_id,
            "Name":student_name,
            "Age":student_age,
            "Email":student_email,
            "Course":student_Course,
            "Semester":student_Semester,
            "Marks":student_marks
        }

        students.append(student)

        print("Student Record Successfully Added")
        print("----------------------------------")
        print("----------------------------------")


    if press==2:
        print("*****Students Record*****")

        for student in students:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Email:", student["Email"])
            print("Course:", student["Course"])
            print("Semester:", student["Semester"])
            print("Marks:", student["Marks"])
            print("-------------------------------")
            print("-------------------------------")


    if press==3:
        if not students:
            print("No Record Found! List is empty")

        else:
            id=int(input("Enter student id you wanna search: "))

            found=False

            for student in students:
                if student["ID"]==id:
                    print(student)
                    print("-------------------------------")
                    print("-------------------------------")
                    found=True

            if not found:
                print("Student Record not Found")
                print("-------------------------------")
                print("-------------------------------")


    if press==4:
        if not students:
            print("No Record Found! List is empty")

        else:
            id=int(input("Enter student id you wanna update his record: "))

            found=False

            for student in students:
                if student["ID"]==id:
                    found=True

                    print("Student Found")

                    print("Press 1 for Updating Name: ")
                    print("Press 2 for Updating Age: ")
                    print("Press 3 for Updating Email: ")
                    print("Press 4 for Updating Course: ")
                    print("Press 5 for Updating Semester: ")
                    print("Press 6 for Updating Marks: ")

                    choice=int(input("Enter Your Choice: "))

                    if choice==1:
                        name=input("Enter Name: ")
                        student["Name"]=name

                    if choice==2:
                        age=int(input("Enter Age: "))
                        student["Age"]=age

                    if choice==3:
                        email=input("Enter Email: ")
                        student["Email"]=email

                    if choice==4:
                        course=input("Enter Course: ")
                        student["Course"]=course

                    if choice==5:
                        semester=int(input("Enter Semester: "))
                        student["Semester"]=semester

                    if choice==6:
                        marks=int(input("Enter Marks: "))
                        student["Marks"]=marks

            if not found:
                print("Student Record Not Found")

    if press==5:
        if not students:
            print("No Record Found! List is empty")

        else:
            id=int(input("Enter student id you wanna delete his record: "))
            found=False

            for student in students:
                if student["ID"]==id:
                    found=True
                    print("Are You Sure? ")
                    print("Enter 1 for yes:")
                    print("Enter 2 for no:")

                    enter=int(input(" "))

                    if enter==1:
                        students.remove(student)
                        print("Student Record Successfully Deleted")
                    else:
                        print("Delete Cancelled")

                    break

            if not found:
                print("Student Record Not Found")


    if press==6:
        if not students:
            print("No Record Found! List is empty")

        else:
            id=int(input("Enter student id you wanna show his result: "))

            found=False

            for student in students:
                if student["ID"]==id:
                    found=True
                    total_marks=100
                    obtained_marks=student["Marks"]
                    percentage = (obtained_marks / total_marks) * 100
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

                    if percentage >= 50:
                        status = "Pass"
                    else:
                        status = "Fail"


                    print("===== STUDENT RESULT =====")
                    print("Name:", student["Name"])
                    print("Student ID:", student["ID"])
                    print("Total Marks:", total_marks)
                    print("Obtained Marks:", obtained_marks)
                    print("Percentage:", percentage, "%")
                    print("Grade:", grade)
                    print("Status:", status)

            if not found:
                print("Student Record Not Found")

    if press==7:
        break
    



