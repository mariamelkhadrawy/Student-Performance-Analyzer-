#Project 2: Student Performance Analyzer
#Build a program to analyze students’ grades.
#Requirements:
#Store students and their grades.
#Calculate each student’s average.
#Display passed and failed students.
#Find the highest average.
#Display all unique subjects.
#Search for a student by name.

students = []

while True:
    print("1- Store students and their grades")
    print("2- Calculate each student's average")
    print("3- Display passed and failed students")
    print("4- Find the highest average")
    print("5- Display all unique subjects")
    print("6- Search for a student by name")
    print("7- Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        grades = {}
        for i in range(3):
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            grades[subject] = grade
        student = {
            "Name" : name ,
            "Grades" : grades ,
        }
        students.append(student)

    elif choice == 2 :
        for student in students :
                grades = student["Grades"]
                average = sum(grades.values()) / len(grades)
                print(student["Name"], average)

    elif choice == 3 :
        for student in students :
            grades = student["Grades"]
            average = sum( grades.values()) / len(grades)
            if average >= 50 :
                print(student["Name"] ,"Student Pass")
            else :
                print(student["Name"] , "Student Fail")

    elif choice == 4 :
        highest = 0
        for student in students:
            grades = student["Grades"]
            average = sum( grades.values()) / len(grades)
            if average > highest:
                highest = average
        print("Higest average is :" , highest)

    elif choice == 5 :
        unique_subjects = set()
        for student in students :
            grades = student["Grades"] 
            for subject in grades.keys() :
                unique_subjects.add(subject)
        print("Unique subjects:", unique_subjects)

    elif choice == 6 :
        search_name = input("Enter name: ")
        found = False
        for student in students:
            if student["Name"] == search_name:
               print(student)
               found = True
               break
        if not found:
            print("Student not found!")

    elif choice == 7 :
        print("GOODBYE")
        break





    












    



 



    


         





    







    


   



    
  


    
    
