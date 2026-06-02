

def validate_task_title(title):
    """Ensure the task title is not empty or just whitespace."""
    if not title or not title.strip():
        print("Error: Task title cannot be empty.")
        return False
    return True


def validate_task_id(task_id, tasks):
    """Ensure the given ID exists in the task list."""
    ids = [task["id"] for task in tasks]
    if task_id not in ids:
        print(f"Error: No task found with ID {task_id}.")
        return False
    return True


def validate_positive_integer(value):
    """Ensure the input can be converted to a positive integer."""
    try:
        num = int(value)
        if num <= 0:
            raise ValueError
        return num
    except ValueError:
        print("Error: Please enter a valid positive number.")
        return None