# validation.py

def validate_task_title(title):
    """Validate that the task title is not empty."""
    if len(title.strip()) == 0:
        raise ValueError("Task title cannot be empty.")
    return True


def validate_task_id(task_id, tasks):
    """Validate that the task ID exists in the task list."""
    ids = [task["id"] for task in tasks]
    if task_id not in ids:
        raise ValueError(f"No task found with ID {task_id}.")
    return True


def validate_positive_integer(value):
    """Validate that the value is a positive integer."""
    try:
        num = int(value)
        if num <= 0:
            raise ValueError("ID must be a positive integer.")
        return num
    except ValueError:
        raise ValueError("Please enter a valid positive number.")