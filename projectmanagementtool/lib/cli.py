import argparse
import json
from lib.models import User, Project, Task

users = {}

def add_user(args):
    users[args.name] = User(args.name)
    print(f"👤 User '{args.name}' created.")

def list_users(args):
    print("\n👥 Users:")
    for user in users:
        print(f"- {user}")

def add_project(args):
    user = users.get(args.user)
    if user:
        project = Project(args.title)
        user.add_project(project)
        print(f"📂 Project '{args.title}' added to user '{args.user}'.")
    else:
        print("❌ User not found.")

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers()

    user_parser = subparsers.add_parser("add-user", help="Create a new user")
    user_parser.add_argument("name")
    user_parser.set_defaults(func=add_user)

    list_parser = subparsers.add_parser("list-users", help="List all users")
    list_parser.set_defaults(func=list_users)

    project_parser = subparsers.add_parser("add-project", help="Add a project to a user")
    project_parser.add_argument("user")
    project_parser.add_argument("title")
    project_parser.set_defaults(func=add_project)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()