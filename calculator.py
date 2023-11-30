import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    new_text = current_text + str(button_value)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for display
entry = tk.Entry(root, width=20, font=("Arial", 14), borderwidth=5)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')'
]

# Add buttons to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 14),
              command=lambda b=button: on_click(b) if b != '=' else calculate_result()).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 14), command=clear_entry).grid(row=row_val, column=col_val, padx=5, pady=5)

# Run the application
root.mainloop()
