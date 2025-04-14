## @file calculator_GUI.py
#  @brief GUI with history and error display
#  @author Šimon Urban
#  
#  This module provides basic user interface for the calculator

## @file
#  @brief GUI-based calculator application using tkinter with support for basic arithmetic and scientific operations
#  @author

from tkinter import *
import os
import sys
import math_lib

## Set working directory to the script's directory to ensure assets like logo.png load correctly
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)

## Calculator State Variables
#  @brief These hold calculator state between user actions
current_input = ""             # @brief Holds the number currently being typed by the user
history_input = "0"            # @brief Stores the visible expression in the history label (e.g., "2+3")
current_operator = None        # @brief Stores the currently selected operator (e.g., '+', '^')
operand = None                 # @brief Stores the left operand for binary operations
just_evaluated = False         # @brief Tracks if the last operation was evaluation (=)

## GUI Window Setup
window = Tk()
window.geometry("480x720")
window.title("Calculator")

## Set application icon using a PNG file
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#E79A3F")

## Display Frame for history and current input
#  @brief This section contains two labels stacked vertically

display_frame = Frame(window, bg="#E79A3F")
display_frame.pack(fill="x", padx=10, pady=10)

## Label showing the previously entered values or result history
history_label = Label(display_frame, text=history_input, anchor="e", font=("Arial", 16), bg="#E79A3F", fg="#444")
history_label.pack(fill="x")

## Label showing the current number input or result
input_label = Label(display_frame, text="0", anchor="e", font=("Arial", 32), bg="#E79A3F", fg="#000")
input_label.pack(fill="x")

## Calculator Button Grid Layout
#  @brief Rows represent groups of calculator buttons
buttons = [
    ["C", "⌫", "", "", ""],
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "^"],
    ["1", "2", "3", "-", "!"],
    ["0", "%", "=", "+", "|x|"]
]

## Frame to contain the button grid
button_frame = Frame(window, bg="#E79A3F")
button_frame.pack(expand=True, fill="both")

## Configure the rows and columns of the button grid to expand equally
for i in range(len(buttons)):
    button_frame.grid_rowconfigure(i, weight=1)
for j in range(5):
    button_frame.grid_columnconfigure(j, weight=1)

## @brief Converts float to int if it's a whole number
#  @param n The number to format
#  @return Integer if whole number, otherwise rounded float

def format_number(n):
    return int(n) if float(n).is_integer() else round(n, 8)

## @brief Clears all calculator state and resets display

def clear_all():
    global current_input, history_input, operand, current_operator, just_evaluated
    current_input = ""
    history_input = "0"
    operand = None
    current_operator = None
    just_evaluated = False
    input_label.config(text="0")
    history_label.config(text=history_input)

## @brief Removes last character from current input

def backspace():
    global current_input
    current_input = current_input[:-1]
    input_label.config(text=current_input if current_input else "0")

## @brief Main handler for all button presses
#  @param value The label of the button pressed

def update_input(value):
    global just_evaluated

    if just_evaluated and value not in {"C", "⌫"}:
        clear_all()

    if value == "C":
        clear_all()
    elif value == "⌫":
        backspace()
    elif value in {"+", "-", "*", "/", "%", "^", "√"}:
        handle_operator(value)
    elif value == "=":
        handle_equal()
    elif value == "|x|":
        handle_abs()
    elif value == "!":
        handle_fact()
    elif value.isdigit() or (value == "-" and not current_input and not operand and not current_operator):
        handle_digit(value)

    input_label.config(text=current_input if current_input else "0")

## @brief Appends digit or sign to current input string
#  @param digit String value representing a digit or negative sign

def handle_digit(digit):
    global current_input
    current_input += digit

## @brief Handles operator button press and stores operand/operator
#  @param op Operator character pressed

def handle_operator(op):
    global current_input, operand, current_operator, history_input

    if op == "-" and not operand and not current_input:
        current_input = "-"
        input_label.config(text=current_input)
        return

    if current_operator and current_input:
        handle_equal(chain=True)

    if current_input:
        operand = float(current_input)
        current_operator = op
        current_input = ""
        history_input = f"{format_number(operand)}{op}"
        history_label.config(text=history_input)
        input_label.config(text="0")

## @brief Executes the stored operation and updates the result
#  @param chain True if part of a chained operation
#  @return Displays result or error message

def handle_equal(chain=False):
    global current_input, operand, current_operator, history_input, just_evaluated

    try:
        if operand is not None and current_input and current_operator:
            second = float(current_input)
            op = current_operator

            if op == "+":
                result = math_lib.add(operand, second)
            elif op == "-":
                result = math_lib.sub(operand, second)
            elif op == "*":
                result = math_lib.mult(operand, second)
            elif op == "/":
                result = math_lib.div(operand, second)
            elif op == "%":
                result = math_lib.modulo(operand, second)
            elif op == "^":
                result = math_lib.n_power(operand, int(second))
            elif op == "√":
                result = math_lib.n_root(second, int(operand))
            else:
                raise ValueError("Invalid operator")

            result = format_number(result)

            if chain:
                operand = float(result)
                current_input = ""
                history_input = f"{result}{op}"
                input_label.config(text="0")
                history_label.config(text=history_input)
            else:
                history_label.config(text=f"{format_number(operand)}{op}{format_number(second)} =")
                input_label.config(text=str(result))
                current_input = str(result)
                operand = None
                current_operator = None
                just_evaluated = True

    except Exception as e:
        input_label.config(text="Error")
        print(f"[Error] {e}")

## @brief Handles absolute value operation (|x|)
#  @return Updates input label with absolute value

def handle_abs():
    global current_input, just_evaluated
    try:
        if current_input:
            result = format_number(math_lib.absolute(float(current_input)))
            current_input = str(result)
            input_label.config(text=current_input)
            just_evaluated = True
    except Exception as e:
        input_label.config(text="Error")
        print("Absolute error:", e)

## @brief Handles factorial operation (!)
#  @return Updates input label with factorial result

def handle_fact():
    global current_input, just_evaluated
    try:
        if current_input:
            result = math_lib.factorial(int(float(current_input)))
            current_input = str(format_number(result))
            input_label.config(text=current_input)
            just_evaluated = True
    except Exception as e:
        input_label.config(text="Error")
        print("Factorial error:", e)

## @brief Create and place calculator buttons
for row_index, row in enumerate(buttons):
    for col_index, label in enumerate(row):
        if not label:
            continue  # Skip empty placeholders
        btn = Button(
            button_frame,
            text=label,
            font=("Arial", 18),
            bg="#F9E0AE",
            activebackground="#F0C674",
            relief=RAISED,
            bd=3,
            command=lambda val=label: update_input(val)
        )
        btn.grid(row=row_index, column=col_index, sticky="nsew", padx=2, pady=2)

## @brief Initialize the label displays
history_label.config(text=history_input)
input_label.config(text="0")

## @brief Start the tkinter main event loop
window.mainloop()

