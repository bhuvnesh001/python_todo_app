import tkinter as tk
from tkinter import messagebox

def add():
    calculate("add")

def subtract():
    calculate("subtract")

def multiply():
    calculate("multiply")

def divide():
    calculate("divide")

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                result = "Error: Divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid Operation"
        
        result_label.config(text=f"Result: {result}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
tk.Button(root, text="Add", command=add).pack(pady=5)
tk.Button(root, text="Subtract", command=subtract).pack(pady=5)
tk.Button(root, text="Multiply", command=multiply).pack(pady=5)
tk.Button(root, text="Divide", command=divide).pack(pady=5)

# Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
