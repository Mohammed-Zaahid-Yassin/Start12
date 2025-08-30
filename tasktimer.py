import time

tasks = []

while True:
    print("\nTask Timer Menu:")
    print("1. Start new timed task")
    print("2. View completed tasks and times")
    print("3. Quit")
    choice = input("Choose an option (1/2/3): ")
  
    if choice == "1":
        task_name = input("Enter the name of the task: ")
        input("Press Enter to start timing...")
        start = time.time()
        input("Press Enter to stop timing...")
        end = time.time()
        duration = end - start
        tasks.append({"task": task_name, "duration": duration})
        print(f"Task '{task_name}' completed in {duration:.2f} seconds.")
    elif choice == "2":
        if not tasks:
            print("No tasks completed yet.")
        else:
            print("\nCompleted Tasks:")
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t['task']}: {t['duration']:.2f} seconds")
    elif choice == "3":
        print("Goodbye! Stay productive.")
        break
    else:
        print("Invalid choice. Please try again.")
