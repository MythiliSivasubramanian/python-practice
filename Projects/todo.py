# Function first
def user_operations(request):
    if request == 1:
        new_tasks = input("Enter the tasks separated by comma : ").split(",")
        all_tasks.extend(new_tasks)
        print("Updated tasks List: ", all_tasks)

    elif request == 2:
        print("Tasks List: ", all_tasks)

    elif request == 3:
        task_index = int(input("Enter the index of the task to be removed: "))
        if 0 <= task_index < len(all_tasks):
            removed = all_tasks.pop(task_index)
            print(f"Removed '{removed}'. Updated list: {all_tasks}")
        else:
            print("Invalid index!")


# Main Program
all_tasks = []

while True:
    tasks = ["Add tasks","View tasks","Remove tasks","Quit"]
    for i, task in enumerate(tasks):
        print(i+1, task)

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input! Enter a number 1-4.")
        continue

    if choice == 4:
        print("Thank you! Goodbye.")
        break

    user_operations(choice)
