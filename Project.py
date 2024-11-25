task_id = [10, 20, 30]
task_title = ["TEST1", "TEST2", "TEST3"]
task_priority = ["High", "Medium", "Low"]
task_deadline = ["1-24-23", "2-25-24", "3-26-25"]
task_completed = ["Complete", "Complete", "Incomplete"]

print("Welcome to To-Do List Manager \n[1] Add Task \n[2] Edit Task \n[3] Delete Task \n[4] Mark Task as Completed \n[5] View Pending Tasks \n[6] View Completed Tasks \n[7] Exit")

while True:
    choose = int(input("Enter Option: "))

    if choose == 1: 
        ids = task_id[-1] + 10  
        title = input("Enter Task Title: ")
        priority = input("Enter Task Priority (High, Medium, Low): ")
        deadline = input("Enter Task Deadline (MM-DD-YYYY): ")

        task_id.append(ids)
        task_title.append(title)
        task_priority.append(priority)
        task_deadline.append(deadline)
        task_completed.append("Incomplete")

        print(task_id)
        print(task_title)
        print(task_priority)
        print(task_deadline)
        print(task_completed)

        print("Task added successfully!")

    elif choose == 2:
        edit_id = int(input("Enter Task ID to Edit: "))
        if edit_id in task_id:
            index = task_id.index(edit_id)
            title = input("Enter New Task Title: ")
            priority = input("Enter New Task Priority (High, Medium, Low): ")
            deadline = input("Enter New Task Deadline (MM/DD/YY): ")

            if title:
                task_title[index] = title
            if priority:
                task_priority[index] = priority
            if deadline:
                task_deadline[index] = deadline

            print("ID :", edit_id)
            print("Tasks: ", title)
            print("Priority: ", priority)
            print("Deadline: ", deadline)
            print("Task updated successfully!")
        else:
            print("Task ID not found!")

    elif choose == 3:  
        remove_id = int(input("Enter ID to Remove: "))
        if remove_id in task_id:
            index = task_id.index(remove_id)
            task_id.remove(remove_id)
            task_title.remove(task_title[index])
            task_priority.remove(task_priority[index])
            task_deadline.remove(task_deadline[index])
            task_completed.remove(task_completed[index])

            print(task_id)
            print(task_title)
            print(task_priority)
            print(task_deadline)
            print(task_completed)
            print("Task removed successfully!")
        else:
            print("Task ID not found!")

    elif choose == 4:
        complete_id = int(input("Enter Task ID to Mark as Completed: "))
        if complete_id in task_id:
            index = task_id.index(complete_id)
            task_completed[index] = "Complete"
            print("Task marked as completed successfully!")
        else:
            print("Task ID not found!")

    elif choose == 5:
        print("\nPending Tasks:")
        found_pending = False  
        for i in range(len(task_id)):
            if task_completed[i] == "Incomplete":
                found_pending = True
                print(f"ID: {task_id[i]}")
                print(f"Title: {task_title[i]}")
                print(f"Priority: {task_priority[i]}")
                print(f"Deadline: {task_deadline[i]}")
                print(f"Completed: No")
        if not found_pending:
            print("No pending tasks.")

    elif choose == 6:
        print("\nCompleted Tasks:")
        for i in range(len(task_id)):
            if task_completed[i] == "Complete":
                print(f"ID: {task_id[i]}")
                print(f"Title: {task_title[i]}")
                print(f"Priority: {task_priority[i]}")
                print(f"Deadline: {task_deadline[i]}")
                print(f"Completed: Yes")

    elif choose == 7:
        choice = input("Are you sure you want to exit the task? Enter (Y)es or (N)o: ")
        if choice.lower() == "y":
            print("Thank you for using To-List Manager")
            break
        else:
            continue
    else:
        print("Welcome to To-Do List Manager \n[1] Add Task \n[2] Edit Task \n[3] Delete Task \n[4] Mark Task as Completed \n[5] View Pending Tasks \n[6] View Completed Tasks \n[7] Exit")