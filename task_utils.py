def add_task(tasks, title):
    task_id = 1 if not tasks else max(task["id"] for task in tasks) + 1

    new_task = {
        "id": task_id,
        "title": title,
        "status": "pending"
    }

    tasks.append(new_task)
    print(f"\n Task '{title}' added successfully with ID {task_id}.")


def mark_task_complete(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "complete":
                print(f"\n Task ID {task_id} is already marked as complete.")
            else:
                task["status"] = "complete"
                print(f"\n Task ID {task_id} ('{task['title']}') marked as complete!")
            return


def view_pending_tasks(tasks):
    pending = [task for task in tasks if task["status"] == "pending"]

    if not pending:
        print("\n No pending tasks. You're all caught up!")
    else:
        print("\n--- Pending Tasks ---")
        for task in pending:
            print(f"  [{task['id']}] {task['title']}")
        print("---------------------")


def track_progress(tasks):
    total = len(tasks)

    if total == 0:
        print("\n No tasks found. Start by adding some tasks!")
        return

    completed = sum(1 for task in tasks if task["status"] == "complete")
    pending = total - completed
    percentage = (completed / total) * 100

    bar_length = 20
    filled = int(bar_length * completed / total)
    bar = "█" * filled + "░" * (bar_length - filled)

    print("\n--- Progress Tracker ---")
    print(f"  Total Tasks   : {total}")
    print(f"  Completed     : {completed}")
    print(f"  Pending       : {pending}")
    print(f"  Progress      : [{bar}] {percentage:.1f}%")
    print("------------------------")


def view_all_tasks(tasks):
    if not tasks:
        print("\n No tasks found. Start by adding some tasks!")
        return

    print("\n--- All Tasks ---")
    for task in tasks:
        status_icon = "✓" if task["status"] == "complete" else "○"
        print(f"  {status_icon} [{task['id']}] {task['title']} ({task['status']})")
    print("-----------------")