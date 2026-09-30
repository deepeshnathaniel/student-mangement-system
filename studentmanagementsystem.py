#mini student management system
students = [{"NAME":"DEEPESH",
             "AGE":"18",
             "DEPARTMENT":"CSE",
             "GPA":8,
             "STUDENT_ID":"2026CSE101"}
            ]

def add_student(name,age,department,gpa):
    students.append({"NAME": name,
                 "AGE": age,
                 "DEPARTMENT": department,
                 "GPA": gpa,
                 "STUDENT_ID":f"2026{department}{len(students) + 100}"})
    print(f"student id == {students[-1]['STUDENT_ID']}")
    return print("student added sucessfully")

def students_list():
    for student in students:
        print("==============================")
        print(f"{'NAME':<12}:{student["NAME"]}")
        print(f"{'AGE':<12}:{student["AGE"]}")
        print(f"{'DEPARTMENT':<12}:{student["DEPARTMENT"]}")
        print(f"{'GPA':<12}:{student["GPA"]}")
        print(f"{'STUDENT_ID':<12}:{student["STUDENT_ID"]}")
        print("==============================")


def student_details(student_id):
    found = False
    for student in students:
        if student_id == student["STUDENT_ID"]:
            found = True
            print(f"{'NAME':<12}:{student["NAME"]}")
            print(f"{'AGE':<12}:{student["AGE"]}")
            print(f"{'DEPARTMENT':<12}:{student["DEPARTMENT"]}")
            print(f"{'GPA':<12}:{student["GPA"]}")
    if not found:
        print("student not found")


def cal_avarage():
    sum_gpa = 0
    avarage = 0
    for student in students:
        gpa = student["GPA"]
        sum_gpa += gpa
        avarage = sum_gpa / len(students)
    return print(f"student avarage gpa is '{avarage:.2f}' of total {len(students)} students")

def show_top_student():
    top_gpa = 0
    for student in students:
        if student["GPA"] > top_gpa:
            top_gpa = student["GPA"]
            student_id = student["STUDENT_ID"]
    return student_details(student_id)

is_running = True
while is_running:
    print("==============================")
    print("      STUDENT MANAGER")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Show Top Student")
    print("6. Exit")
    print("==============================")

    option = input("enter your choice: ")
    if not option.isalpha():
        option = int(option)
        if option == 1:
            print("==============================")
            name = input("enter student name: ").upper()
            age = input("enter student age: ")
            department = input("enter student department: ").upper()
            while True:
                try:
                    gpa = float(input("enter student GPA:"))
                    if gpa>0 and gpa<=10:
                        break
                    else:
                        print("enter correct GPA")
                except ValueError:
                    print("invalid GPA")

            add_student(name, age, department, gpa)


        if option == 2:
            students_list()

        if option == 3:
            print("==============================")
            student_id = input("enter student id: ").upper()
            student_details(student_id)

        if option == 4:
            print("==============================")
            cal_avarage()
            print("==============================")

        if option == 5:
            print("==============================")
            show_top_student()
            print("==============================")

        if option == 6:
            is_running = False
            print("==============================")
            print("        THANK YOU")
            print("==============================")

    else:
        print("invalid option")

