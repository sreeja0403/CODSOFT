# task_manager.py
class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def update_task(self, index, title=None, description=None):
        if 0 <= index < len(self.tasks):
            if title is not None:
                self.tasks[index].title = title
            if description is not None:
                self.tasks[index].description = description

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
