"""
Simple To-Do List Manager
1. Add task
2. View all tasks
3. Mark task as completed
4. Delete task
5. Exit
Tasks are saved in a text file ('tasks.txt').
"""


import os

# Tasks are saved in a text file ('tasks.txt').
TASK_FILE = "tasks.txt"
# tasks.txt will be created in the same folder of this .py file

# Load tasks from TASK_FILE. Empty list if file not found.
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f: # With open doesnt need to close file again
        return [line.strip() for line in f.readlines()]

#  Save tasks to TASK_FILE.
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.write("\n".join(tasks))

def main():
    tasks = load_tasks()
    # Main menu loop for the To-Do List Manager.
    while True: 
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)

        elif choice == "2":
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

        elif choice == "3":
            index = int(input("Task number to complete: ")) - 1
            tasks[index] = tasks[index] + " (Completed)"
            save_tasks(tasks)

        elif choice == "4":
            index = int(input("Task number to delete: ")) - 1
            tasks.pop(index)
            save_tasks(tasks)

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
