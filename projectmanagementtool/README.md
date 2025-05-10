# Project Management CLI Tool

## Overview  
This Python-based Command-Line Interface (CLI) tool helps to efficiently organize projects and tasks. With structured commands, you can create users, assign projects, track task completion, and persist data using JSON.

## Features  
- Create and list users  
- Assign projects to users  
- Add tasks to projects  
- Mark tasks as complete  
- Save and load data using JSON  

## Installation  
Ensure Python is installed. Then, clone the repository and install dependencies:

```bash
git clone <repo-url>
cd project-management-tool
pip install -r requirements.txt

To initialize:
# Add user  
python lib/cli.py add-user Mike  

# List users  
python lib/cli.py list-users  

# Add project to a user  
python lib/cli.py add-project Mike "Backend Refactor"  

# Add a task to project  
python lib/cli.py add-task Mike "Optimize database queries"  

# Mark task complete  
python lib/cli.py complete-task Mike "Optimize database queries"  

#File Structure
project-management-tool/
│── lib/
│   │── __init__.py   # Package marker
│   │── models.py     # Defines User, Project, Task classes
│   │── cli.py        # Handles CLI logic using argparse
│   │── data.json     # Stores persisted project/task data
│── tests/
│   │── test_models.py  # Unit tests
│── requirements.txt  # Dependencies
│── README.md        # Documentation

#Test to run:
python3 -m unittest discover tests