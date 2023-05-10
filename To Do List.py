import tkinter as tk

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        task_listbox.insert(selected_task, f"[Done] {task}")

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=2, column=0, padx=10, pady=10)

mark_completed_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
mark_completed_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()