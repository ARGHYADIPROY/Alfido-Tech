import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Task entry and Add task button
        entry_frame = tk.Frame(root)
        entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(entry_frame, width=70)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        add_button = tk.Button(entry_frame, text="Add Task", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=5)

        # Task listbox
        self.task_listbox = tk.Listbox(root, width=80, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons frame
        buttons_frame = tk.Frame(root)
        buttons_frame.pack(pady=10)

        # Delete task button
        delete_button = tk.Button(buttons_frame, text="Delete Task", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, padx=5)

        # Mark as completed button
        complete_button = tk.Button(buttons_frame, text="Mark as Completed", command=self.mark_completed)
        complete_button.pack(side=tk.LEFT, padx=5)

        # Quit button
        quit_button = tk.Button(root, text="Quit", command=root.destroy)
        quit_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            messagebox.showinfo("Task Completed", f"The task '{task}' is marked as completed.")
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
