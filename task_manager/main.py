# main.py

from task_utils import add_task, mark_task_complete, view_pending_tasks, track_progress
from validation import validate_task_title, validate_task_id, validate_positive_integer

def display_menu():
    print("\n===== Task Manager =====")
    print("1. Add a task")
    print("2. Mark task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. Exit")
    print("========================")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ")
            try:
                validate_task_title(title)
                tasks = add_task(tasks, title)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            raw_id = input("Enter task ID to mark complete: ")
            try:
                task_id = validate_positive_integer(raw_id)
                validate_task_id(task_id, tasks)
                tasks = mark_task_complete(tasks, task_id)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            track_progress(tasks)

        elif choice == "5":
            print("Goodbye! Stay productive!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()