# student list
studid = [1]
studname = ["student1"]
studGender = ["Male"]
studAge = [23]

# enrollment system
print("Welcome to phinma-coc \n1. New student \n2. Old Student")
choose = int(input("Only number: \nEx. 1 or 2\nEnter here: "))

if choose == 1:
    ids = input("Enter student ID: ")
    name = input("Enter student name: ")
    gender = input("Enter student gender (Male/Female): ")
    age = int(input("Enter student age: "))
    studid.append(ids)
    studname.append(name)
    studGender.append(gender)
    studAge.append(age)
    print("Student added successfully!")
    print(studid)
    print(studname)
    print(studGender)
    print(studAge)
elif choose == 2:
    search = int(input("Search student ID: "))
    if search in studid:
        index = studid.index(search)
        print("Student found!")
        print("ID:", studid[index])
        print("Name:", studname[index])
        print("Gender:", studGender[index])
        print("Age:", studAge[index])
    else:
        print("Student not found")
else:
    print("Please try again")