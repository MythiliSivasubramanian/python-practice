import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.write("\n".join(tasks))

def main():
    tasks = load_tasks()

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
