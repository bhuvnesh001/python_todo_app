import os

DATA_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        file.writelines(task + "\n" for task in tasks)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not allowed.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a number.")

def mark_task_done(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            if not tasks[index].startswith("[✓] "):
                tasks[index] = "[✓] " + tasks[index]
                print("Marked as done.")
            else:
                print("Task already marked done.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a number.")

def menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def main():
    tasks = load_tasks()
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
