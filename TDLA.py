import json
import os

# Global variable to store tasks
tasks = []

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)

def save_tasks():
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, due_date=""):
    task = {"description": description, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_tasks()
    print(f'Task "{description}" added.')

def view_tasks():
    if tasks:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "To-Do"
            due_date = f' (Due: {task["due_date"]})' if task["due_date"] else ''
            print(f'{index}. [{status}] {task["description"]}{due_date}')
        print("-----------------------\n")
    else:
        print("Your to-do list is empty.")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        save_tasks()
        print(f'Task "{tasks[task_index - 1]["description"]}" marked as complete.')
    else:
        print("Invalid task number.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        save_tasks()
        print(f'Task "{deleted_task["description"]}" deleted.')
    else:
        print("Invalid task number.")

def main():
    load_tasks()
    while True:
        print("\n===== To-Do List Application =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, press Enter to skip): ")
            add_task(description, due_date)
        elif choice == '3':
            view_tasks()
            task_index = int(input("Enter task number to mark as complete: "))
            complete_task(task_index)
        elif choice == '4':
            view_tasks()
            task_index = int(input("Enter task number to delete: "))
            delete_task(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
