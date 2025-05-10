import json

class User:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

class Task:
    def __init__(self, description, contributors=[]):
        self.description = description
        self.completed = False
        self.contributors = contributors

    def mark_complete(self):
        self.completed = True