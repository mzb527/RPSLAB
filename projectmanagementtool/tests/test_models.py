import unittest
from lib.models import User, Project, Task

class TestProjectManagement(unittest.TestCase):
    def test_create_user(self):
        user = User("Mike")
        self.assertEqual(user.name, "Mike")
        self.assertEqual(len(user.projects), 0)  # No projects yet

    def test_add_project(self):
        user = User("Mike")
        project = Project("Backend Refactor")
        user.add_project(project)
        self.assertIn(project, user.projects)
        self.assertEqual(len(user.projects), 1)  # Should have one project now

    def test_create_task(self):
        task = Task("Write documentation")
        self.assertEqual(task.description, "Write documentation")
        self.assertFalse(task.completed)  # Task should start as incomplete

    def test_complete_task(self):
        task = Task("Fix bugs")
        task.mark_complete()
        self.assertTrue(task.completed)  # Task should be marked as complete

if __name__ == "__main__":
    unittest.main()