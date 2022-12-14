# Simple Calculator using tkinter GUI and Python.
#
# Import the needed modules.
import tkinter as tk
from tkinter import messagebox


# Get a valid number from user in the Entry field:
def get_number(entry):
    string = entry.get()
    try:
        value = float(string) 
    except ValueError:
        return None # If value is not int or float, then is invalid.
    return value


# Evaluate Button's behavior when it's clicked by user:
def evaluate_click():
    # In case of invalid numbers, show errors messages\
    # and focus on the Entry that contain the invalid number.
    value_1 = get_number(entry_1)
    if value_1 is None:
        messagebox.showerror("Error", "Invalid value in the first field!")
        entry_1.focus_set()
        return
    value_2 = get_number(entry_2)
    if value_2 is None:
        messagebox.showerror("Error", "Invalid value in the second field!")
        entry_2.focus_set()
        return
    operation = op.get()

    # If operation is Division(radiobutton with value=4), \
    # show the Error and\
    # focus the Entry_2 that contain the zero.
    if operation == 4 and value_2 == 0:
        messagebox.showerror("Error", "Cannot divide by zero!")
        entry_2.focus_set()
        return

    # In case of valid numbers, show the result of operations\
    # (Addition, Substraction, Multiplication, Division)\
    # (radiobuttons with value=1, value=2, value=3, value=4).
    if operation == 1:
        result = value_1 + value_2
    elif operation == 2:
        result = value_1 - value_2
    elif operation == 3:
        result = value_1 * value_2
    else:
        result = value_1 / value_2
    messagebox.showinfo("Result", str(result))


# Create a main window for the application.
win = tk.Tk()
# Create the title of the application and center it.
blank_space = ' '
win.title(20 * blank_space + 'Calculator')

# Create first entry input field.
entry_1 = tk.Entry(win)

# Create the 4 radiobuttons for our 4 operations and\
# set the first one as selected when application starts.
op = tk.IntVar()
op_add = tk.Radiobutton(win, text= '+', variable=op, value=1) # Addition
op_add.select()
op_sub = tk.Radiobutton(win, text= '-', variable=op, value=2) # Substraction
op_mul = tk.Radiobutton(win, text= '*', variable=op, value=3) # Multiplication
op_div = tk.Radiobutton(win, text= '/', variable=op, value=4) # Division

# Create second entry input field.
entry_2 = tk.Entry(win)

# Create the Evaluation button and assign a callback (evaluate_click) to it\
# so the button ca act according to the behavior set using evaluate_click().
eval_button = tk.Button(win, text = 'Evaluate', command=evaluate_click)

# Place all widgets inside the main window using grid() method and \
# set the focus on Entry 1 input field using focus_set().
entry_1.grid(row=0, rowspan=4, column=0)
entry_1.focus_set()

op_add.grid(row=0, column=1)
op_sub.grid(row=1, column=1)
op_mul.grid(row=2, column=1)
op_div.grid(row=3, column=1)

entry_2.grid(row=0, rowspan=4, column=2)

eval_button.grid(row=4, columnspan=3)

# Display the main window and end the Application.
win.mainloop()


