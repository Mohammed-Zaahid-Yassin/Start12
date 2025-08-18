def view_file(filename):
    try:
        with open(filename, 'r') as file:
            print("\nFile contents:\n")
            for line in file:
                print(line.rstrip())
    except FileNotFoundError:
        print("File not found.")
def append_to_file(filename):
    line = input("Enter a line to append: ")
    with open(filename, 'a') as file:
        file.write(line + '\n')
    print("Line appended.")
def overwrite_file(filename):
    print("Enter new content (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    with open(filename, 'w') as file:
        for l in lines:
            file.write(l + '\n')
    print("File overwritten.")
filename = input("Enter the filename to manipulate: ")
while True:
    print("\nOptions:")
    print("1. View file")
    print("2. Append line")
    print("3. Overwrite file")
    print("4. Quit")

    choice = input("Choose (1/2/3/4): ")
    if choice == "1":
        view_file(filename)
    elif choice == "2":
        append_to_file(filename)
    elif choice == "3":
        overwrite_file(filename)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid option.")
