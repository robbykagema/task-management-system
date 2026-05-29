def validate_task_title(title):
    title = title.strip()

    if not title:
        return False, "Task title cannot be empty. Please enter a valid title."

    if len(title) > 100:
        return False, "Task title is too long. Please keep it under 100 characters."

    return True, title


def validate_task_id(task_id_input, tasks):
    if not task_id_input.strip().isdigit():
        return False, "Invalid input. Please enter a numeric task ID."

    task_id = int(task_id_input.strip())

    task_ids = [task["id"] for task in tasks]
    if task_id not in task_ids:
        return False, f"Task with ID {task_id} not found. Please try again."

    return True, task_id


def validate_menu_choice(choice, valid_options):
    if choice.strip() not in valid_options:
        return False, f"Invalid choice. Please enter one of: {', '.join(valid_options)}"

    return True, choice.strip()