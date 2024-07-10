import os

TASK_FILE = 'tasks.txt'
LOG_FILE = 'activity_log.txt'


def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            tasks = file.read().splitlines()
    else:
        tasks = []
    return tasks


def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def log_activity(activity):
    """Log activity to the log file."""
    with open(LOG_FILE, 'a') as file:
        file.write(activity + '\n')


def create_task(task):
    tasks = load_tasks()
    if task in tasks:
        message = f'created "{task}" - unsuccessful (task already exists)'
        print(message)
        log_activity(message)
    else:
        tasks.append(task)
        save_tasks(tasks)
        message = f'created "{task}" - successful'
        print(message)
        log_activity(message)


def remove_task(task):
    tasks = load_tasks()
    if task not in tasks:
        message = f'removed "{task}" - unsuccessful (task does not exist)'
        print(message)
        log_activity(message)
    else:
        tasks.remove(task)
        save_tasks(tasks)
        message = f'removed "{task}" - successful'
        print(message)
        log_activity(message)


def search_task(task):
    tasks = load_tasks()
    if task in tasks:
        message = f'searched "{task}" - found'
        print(message)
        log_activity(message)
    else:
        message = f'searched "{task}" - not found'
        print(message)
        log_activity(message)


def print_all_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks present.")
    else:
        print("Existing tasks:")
        for task in tasks:
            print(f"- {task}")


def main():
    while True:
        print("\nTask Manager")
        print("1. Create a new task")
        print("2. Remove an existing task")
        print("3. Search for a task")
        print("4. Print all tasks")
        print("5. Exit")

        s = input("Enter your choice: ")

        if s == '1':
            task = input("Enter the task to create: ").strip()
            if task:
                create_task(task)
            else:
                print("Task cannot be empty.")
        elif s == '2':
            task = input("Enter the task to remove: ").strip()
            if task:
                remove_task(task)
            else:
                print("Task cannot be empty.")
        elif s == '3':
            task = input("Enter the task to search for: ").strip()
            if task:
                search_task(task)
            else:
                print("Task cannot be empty.")
        elif s == '4':
            print_all_tasks()
        elif s == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()
