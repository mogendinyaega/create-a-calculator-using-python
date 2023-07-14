import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title(" MRT Calculator")

# Set the background color to blue
root.configure(background="grey")

# Create an Entry widget for displaying digits and sums
entry = tk.Entry(root, width=30, justify="right", bd=5)
entry.grid(row=0, column=0, columnspan=4)


# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


# Function to handle the equal button
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Create buttons for digits and operators
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    (".", 4, 0),
    ("0", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
    ("!", 5, 0),
    ("(", 5, 1),
    (")", 5, 2),
    ("00", 5, 3)
]

# Create the buttons and assign the button_click function to their command
for button_text, row, col in buttons:
    button = tk.Button(root, text=button_text, width=5, height=2,
                       command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=col)

# Create the equal button separately to assign the button_equal function to its command
equal_button = tk.Button(root, text="=", width=5, height=2,
                         command=button_equal)
equal_button.grid(row=4, column=2)

# Start the tkinter event loop
root.mainloop()
