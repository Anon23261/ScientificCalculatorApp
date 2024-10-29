import tkinter as tk
import math

# Initialize the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry to display the calculation
entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=5)

# Function to insert numbers and operators
def insert(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Scientific functions
def sqrt():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.sqrt(value))

def sin():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.sin(math.radians(value)))

def cos():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.cos(math.radians(value)))

def tan():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.tan(math.radians(value)))

def log():
    value = float(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.log10(value))

def factorial():
    value = int(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, math.factorial(value))

def quadratic_formula(a, b, c):
    try:
        d = (b ** 2) - (4 * a * c)
        sol1 = (-b - math.sqrt(d)) / (2 * a)
        sol2 = (-b + math.sqrt(d)) / (2 * a)
        entry.delete(0, tk.END)
        entry.insert(0, f"{sol1}, {sol2}")
    except ValueError:
        entry.insert(0, "Invalid values")

def area_circle(radius):
    entry.delete(0, tk.END)
    entry.insert(0, math.pi * radius ** 2)

def pythagorean_theorem(a, b):
    entry.delete(0, tk.END)
    entry.insert(0, math.sqrt(a**2 + b**2))

# Layout the buttons
button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("Clear", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("√", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("x²", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3), ("=", 4, 4),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3), ("!", 5, 4),
]

for (text, row, col) in button_texts:
    action = lambda x=text: insert(x) if x not in ["Clear", "√", "x²", "sin", "cos", "tan", "log", "!", "="] else None
    if text == "=":
        action = calculate
    elif text == "Clear":
        action = clear
    elif text == "√":
        action = sqrt
    elif text == "sin":
        action = sin
    elif text == "cos":
        action = cos
    elif text == "tan":
        action = tan
    elif text == "log":
        action = log
    elif text == "!":
        action = factorial
    elif text == "x²":
        action = lambda: insert("**2")
    button = tk.Button(root, text=text, width=5, height=2, command=action)
    button.grid(row=row, column=col)

# Additional formula buttons
tk.Button(root, text="Quadratic", width=5, height=2, command=lambda: quadratic_formula(1, -3, 2)).grid(row=6, column=0)
tk.Button(root, text="Circle Area", width=5, height=2, command=lambda: area_circle(5)).grid(row=6, column=1)
tk.Button(root, text="Pythagorean", width=5, height=2, command=lambda: pythagorean_theorem(3, 4)).grid(row=6, column=2)

root.mainloop()
