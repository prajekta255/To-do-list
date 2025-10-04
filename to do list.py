import tkinter as tk
from tkinter import messagebox

# Functions
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks_listbox.delete(selected)
            tasks_listbox.insert(selected, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Updated task cannot be empty!")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Main window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.configure(bg="#f5f5f5")

# Task Entry
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", width=12, command=add_task, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Task", width=12, command=update_task, bg="#FFC107", fg="black")
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task, bg="#F44336", fg="white")
delete_button.grid(row=0, column=2, padx=5)

# Task Listbox
tasks_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
tasks_listbox.pack(pady=10)

# Run the app
root.mainloop()