from task_utils import (
    add_task,
    mark_task_complete,
    view_pending_tasks,
    track_progress,
    view_all_tasks
)
from validation import (
    validate_task_title,
    validate_task_id,
    validate_menu_choice
)


def display_menu():
    print("\n=============================")
    print("     TASK MANAGEMENT SYSTEM  ")
    print("=============================")
    print("  1. Add a new task")
    print("  2. Mark a task as complete")
    print("  3. View pending tasks")
    print("  4. View all tasks")
    print("  5. Track progress")
    print("  6. Exit")
    print("=============================")


def main():
    tasks = []
    valid_options = ["1", "2", "3", "4", "5", "6"]

    print("\nWelcome to your Task Manager!")

    while True:
        display_menu()
        choice_input = input("Enter your choice: ")

        is_valid, result = validate_menu_choice(choice_input, valid_options)
        if not is_valid:
            print(f"\n {result}")
            continue

        choice = result

        if choice == "1":
            title_input = input("\nEnter task title: ")
            is_valid, result = validate_task_title(title_input)
            if not is_valid:
                print(f"\n {result}")
            else:
                add_task(tasks, result)

        elif choice == "2":
            if not tasks:
                print("\n No tasks available to mark as complete.")
            else:
                view_all_tasks(tasks)
                id_input = input("Enter the task ID to mark as complete: ")
                is_valid, result = validate_task_id(id_input, tasks)
                if not is_valid:
                    print(f"\n {result}")
                else:
                    mark_task_complete(tasks, result)

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            view_all_tasks(tasks)

        elif choice == "5":
            track_progress(tasks)

        elif choice == "6":
            print("\nGoodbye! Keep being productive. 👋\n")
            break


if __name__ == "__main__":
    main()