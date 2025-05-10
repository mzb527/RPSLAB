# task_manager/task_utils.py

from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

def add_task(task_list, title, description, due_date):
    """Add a new task to the task list."""
    task = {
        "title": validate_task_title(title),
        "description": validate_task_description(description),
        "due_date": validate_due_date(due_date),
        "completed": False
    }
    task_list.append(task)
    print(f"Task '{title}' added successfully.")

def mark_task_as_complete(task_list, title):
    """Mark a task as complete by title."""
    for task in task_list:
        if task["title"] == title:
            task["completed"] = True
            print(f"Task '{title}' marked as complete.")
            return
    print(f"Task '{title}' not found.")

def view_pending_tasks(task_list):
    """View all pending tasks."""
    print("Pending Tasks:")
    for task in task_list:
        if not task["completed"]:
            print(f"- {task['title']} (Due: {task['due_date']}): {task['description']}")
    print("-" * 50)

def calculate_progress(task_list):
    """Calculate and display the progress of completed tasks."""
    total_tasks = len(task_list)
    if total_tasks == 0:
        print("No tasks available to calculate progress.")
        return
    completed_tasks = sum(task["completed"] for task in task_list)
    progress = (completed_tasks / total_tasks) * 100
    print(f"Progress: {completed_tasks}/{total_tasks} tasks completed ({progress:.2f}%).")