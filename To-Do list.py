tasks =  []

while True:
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = int(input("Enter Your Choice-> "))

    if choice == 1:
        task = input("Enter A Task-> ")
        tasks.append(task)
        print("Task Added")
    elif choice == 2:
        print("Your Tasks")
        for task in tasks:
            print(task)
    elif choice == 3:
        task_to_remvove = input("Enter The Task To Remove-> ")
        if task_to_remvove in tasks:
            tasks.remove(task_to_remvove)
            print("Task Removed")
        else:
            print("Task Not Found")
    elif choice == 4:
        print('Exiting....')
        break
    else:
        print("Invalid Choice. Try Again")

        