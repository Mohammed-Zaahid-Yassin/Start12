# Simple To-Do List App

todo = []

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task: ")
        todo.append(task)
        print("Task added!")
    elif choice == '2':
        print("Your To-Do List:")
        for idx, item in enumerate(todo, 1):
            print(f"{idx}. {item}")
        if not todo:
            print("No tasks yet.")
    elif choice == '3':
        if not todo:
            print("No tasks to remove.")
            continue
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(todo):
            removed = todo.pop(num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
