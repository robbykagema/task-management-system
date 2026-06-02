# task_utils.py

def add_task(tasks, title):
    """Add a new task to the task list."""
    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id":     new_id,
        "title":  title.strip(),
        "status": "pending"
    }
    tasks.append(new_task)
    print(f"Task '{title.strip()}' added successfully.")
    return tasks


def mark_task_complete(tasks, task_id):
    """Mark a task as completed by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            print(f"Task {task_id} marked as complete.")
            return tasks
    return tasks


def view_pending_tasks(tasks):
    """Display all pending tasks."""
    pending = [task for task in tasks if task["status"] == "pending"]
    if not pending:
        print("No pending tasks.")
    else:
        print("\n--- Pending Tasks ---")
        for task in pending:
            print(f"  [{task['id']}] {task['title']}")
        print("---------------------")
    return pending


def track_progress(tasks):
    """Track and display task completion progress."""
    total     = len(tasks)
    completed = sum(1 for task in tasks if task["status"] == "completed")
    pending   = total - completed

    print("\n--- Progress ---")
    print(f"Total tasks : {total}")
    print(f"Completed   : {completed}")
    print(f"Pending     : {pending}")
    if total > 0:
        percent = (completed / total) * 100
        print(f"Progress    : {percent:.1f}%")
    print("----------------")