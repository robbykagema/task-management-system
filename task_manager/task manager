

from task_utils import add_task, mark_task_complete, view_pending_tasks, track_progress
from validation import validate_task_title, validate_task_id, validate_positive_integer

def display_menu():
    """Print the main menu."""
    print("\n===== Task Manager =====")
    print("1. Add a task")
    print("2. Mark task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. Exit")
    print("========================")

def main():
    tasks = []  # All tasks live here as a list of dicts

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        # --- Option 1: Add a task ---
        if choice == "1":
            title = input("Enter task title: ")
            if validate_task_title(title):
                tasks = add_task(tasks, title)

        # --- Option 2: Mark as complete ---
        elif choice == "2":
            raw_id = input("Enter task ID to mark complete: ")
            task_id = validate_positive_integer(raw_id)
            if task_id and validate_task_id(task_id, tasks):
                tasks = mark_task_complete(tasks, task_id)

        # --- Option 3: View pending tasks ---
        elif choice == "3":
            view_pending_tasks(tasks)

        # --- Option 4: Track progress ---
        elif choice == "4":
            track_progress(tasks)

        # --- Option 5: Exit ---
        elif choice == "5":
            print("Goodbye! Stay productive!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()