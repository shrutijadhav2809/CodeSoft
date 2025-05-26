tasks = []


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'Task "{task}" has been added.')


def list_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def delete_task():
    list_tasks()
    if not tasks:
        return

    try:
        task_to_delete = int(input("Enter the task number to delete: "))
        if 1 <= task_to_delete <= len(tasks):
            removed_task = tasks.pop(task_to_delete - 1)
            print(f'Task "{removed_task}" has been deleted.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    print("Welcome to the To-Do List Application.")

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. View all tasks")
        print("4. Exit")

        choice = input("Enter your choice): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Exiting the application. Goodbye.")
            break
        else:
            print("Invalid choice.")
