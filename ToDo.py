import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, f"[ ] {task}")
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_as_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        if "[ ]" in task:
            listbox.delete(selected_task_index)
            listbox.insert(tk.END, task.replace("[ ]", "[X]"))
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def clear_all_tasks():
    listbox.delete(0, tk.END)
    save_tasks()

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass 


root = tk.Tk()
root.title("To-Do List App")


entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed)
complete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks)
clear_button.pack(pady=5)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(pady=10)


load_tasks()


root.mainloop()
