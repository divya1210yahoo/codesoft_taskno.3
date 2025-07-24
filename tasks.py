import tkinter as tk
from tkinter import messagebox
import json
import os
FILE_NAME = "tasks.json"
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
def update_listbox():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "✔️" if task["completed"] else "❌"
        listbox.insert(tk.END, f"{status} {task['task']}")
def complete_task():
    try:
        index = listbox.curselection()[0]
        tasks[index]["completed"] = True
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark complete.")
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
root = tk.Tk()
root.title("To-Do List App")
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)
listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
listbox.pack(pady=10)
button_frame = tk.Frame(root)
button_frame.pack()

complete_button = tk.Button(button_frame, text="Mark Completed", command=complete_task)
complete_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=1, padx=10)
tasks = load_tasks()
update_listbox()

root.mainloop()
