# main.py

from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    task_list = []

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. Calculate Progress")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                title = input("Enter task title: ").strip()
                description = input("Enter task description: ").strip()
                due_date = input("Enter due date (YYYY-MM-DD): ").strip()
                add_task(task_list, title, description, due_date)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                title = input("Enter task title to mark complete: ").strip()
                mark_task_as_complete(task_list, title)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            view_pending_tasks(task_list)

        elif choice == "4":
            calculate_progress(task_list)

        elif choice == "5":
            print("Exiting Task Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()