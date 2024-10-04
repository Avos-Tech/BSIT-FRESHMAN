# person list
id = [0, 1, 2]
fname = ["test1", "test2", "test3"]
mname = ["B", "C", "A"]
lname = ["Smith", "Wick", "Kulas"]
age = [15, 4, 63]
ageStatus = ["Young", "Child", "Senior"]
ageCategory = ["0-5 Child", "6-17 Young", "18-60 Adult", "61-120 Senior"]

# main program
print("Welcome to Personal Information \n1. New person \n2. Search Person \n3. Show Current Data \n4. Exit")
choose = int(input("Only number: \nEx. 1, 2, 3, or 4\nEnter here: "))
while choose != 4:
    if choose == 1:
        new_id = int(input("Enter person ID: "))
        new_fname = input("Enter person first name: ")
        new_mname = input("Enter person middle name: ")
        new_lname = input("Enter person last name: ")
        new_age = int(input("Enter person age: "))
        
        if 0 <= new_age <= 5:
            new_ageStatus = "Child"
            new_ageCategory = "0-5 Child"
        elif 6 <= new_age <= 17:
            new_ageStatus = "Young"
            new_ageCategory = "6-17 Young"
        elif 18 <= new_age <= 60:
            new_ageStatus = "Adult"
            new_ageCategory = "18-60 Adult"
        else:
            new_ageStatus = "Senior"
            new_ageCategory = "61-120 Senior"
        id.append(new_id)
        fname.append(new_fname)
        mname.append(new_mname)
        lname.append(new_lname)
        age.append(new_age)
        ageStatus.append(new_ageStatus)
        ageCategory.append(new_ageCategory)
        print("Person added successfully!")
        print(id)
        print(fname)
        print(mname)
        print(lname)
        print(age)
        print(ageStatus)
        print(ageCategory)
    elif choose == 2:
        search_id = int(input("Search person ID: "))
        if search_id in id:
            index = id.index(search_id)
            print("Person found!")
            print("ID:", id[index])
            print("First Name:", fname[index])
            print("Middle Name:", mname[index])
            print("Last Name:", lname[index])
            print("Age:", age[index])
            print("Age Status:", ageStatus[index])
            print("Age Category:", ageCategory[index])
        else:
            print("Person not found")
    elif choose == 3:
        print("Current Data:")
        for i in range(len(id)):
            print("ID:", id[i])
            print("First Name:", fname[i])
            print("Middle Name:", mname[i])
            print("Last Name:", lname[i])
            print("Age:", age[i])
            print("Age Status:", ageStatus[i])
            print("Age Category:", ageCategory[i])
            print()        
    else:
        print("Please try again") 
    print("Welcome to Personal Information")
    choose = int(input("Only number: \nEx. 1, 2, 3, or 4\nEnter here: "))