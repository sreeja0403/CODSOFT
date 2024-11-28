# gui_todo.py
import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.manager = TaskManager()
        master.title("To-Do List Application")

        self.task_listbox = tk.Listbox(master, width=50, height=15)
        self.task_listbox
