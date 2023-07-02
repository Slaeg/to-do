import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.tasks = [] # Initialize an empty list to store tasks

        # Set up the main application window
        self.root = root
        self.root.geometry('300x400')
        self.root.title('To-Do List')

        # Frame to display the tasks
        self.tasks_frame = tk.Frame(self.root)
        self.tasks_frame.pack()

        # Entry field to add or delete tasks
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        # Button to add a task
        self.add_task_button = tk.Button(self.root, text='Add Task', command=self.add_task)
        self.add_task_button.pack()

        # Buttton to delete a task
        self.delete_task_button = tk.Button(self.root, text='Delete Task', command=self.delete_task)
        self.delete_task_button.pack()

    # Function to add a task
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_tasks_frame()

    # Function to delete a task
    def delete_task(self):
        task_to_delete = self.task_entry.get()
        if task_to_delete in self.tasks:
            self.tasks.remove(task_to_delete)
            self.task_entry.delete(0, tk.END)
            self.update_tasks_frame()
        else:
            messagebox.showerror('Error', 'Task not found')

    # Function to update the task display
    def update_tasks_frame(self):
        # Clear all current tasks from the display
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        # Add each task in the task list to the display
        for task in self.tasks:
            task_label = tk.Label(self.tasks_frame, text=task)
            task_label.pack()

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
