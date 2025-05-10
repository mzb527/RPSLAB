# This module contains validation functions for the ToDo list application.
from datetime import datetime

def validate_task_title(title):
    """Ensure that the title is non-empty and at least 3 characters long."""
    if not title.strip():
        raise ValueError("Title cannot be empty.")
    if len(title) < 3:
        raise ValueError("Title must be at least 3 characters long.")
    return title

def validate_task_description(description):
    """Ensure that the description is non-empty."""
    if not description.strip():
        raise ValueError("Description cannot be empty.")
    return description

def validate_due_date(due_date):
    """Ensure the due date is in the correct format (YYYY-MM-DD) and is valid."""
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in the format YYYY-MM-DD.")
    return due_date