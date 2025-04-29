## @file calculator_GUI.py
#  @brief GUI with history and error display
#  @author Šimon Urban
#  
#  This module provides basic user interface for the calculator

from tkinter import *
from tkinter import messagebox
import os
import sys
import math_lib

## Determine the correct path for assets depending on whether it's running from source or a bundled executable
if getattr(sys, 'frozen', False):
    script_dir = sys._MEIPASS
else:
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

## Set working directory to the script's directory to ensure assets like logo.png load correctly
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
# Set application background colour
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.config(background="#a68d8d")

## Display Frame for history and current input
#  @brief This section contains two labels stacked vertically

display_frame = Frame(window, bg="#a68d8d")
display_frame.pack(fill="x", padx=0, pady=10)

## Outer frame to modify the height of the vertical height of the buttons
# @brief Frame to limit button area
outer_frame = Frame(window, bg="#a68d8d")
outer_frame.pack(expand=False, fill="x")

## @brief Frame to contain the button grid
button_frame = Frame(outer_frame, bg="#a68d8d", height=125)
button_frame.pack(expand=False, fill="both")


## Label showing the previously entered values or result history
#  Located on the top of the display_frame
history_label = Label(display_frame, text=history_input, anchor="e", font=("Arial", 26), bg="#a68d8d", fg="#444")
history_label.pack(fill="x")

## Label showing the current number input or result
#  Located on the bottom of the display_frame
input_label = Label(display_frame, text="0", anchor="e", font=("Arial", 40), bg="#a68d8d", fg="#000")
input_label.pack(fill="x")

## Calculator Button Grid Layout
#  @brief Rows represent groups of calculator buttons


buttons = [
    ["?", "⌫", "C", "!", "%"],
    ["7", "8", "9", "+", "-"],
    ["4", "5", "6", "*", "/"],
    ["1", "2", "3", "√", "^"],
    [".", "0", "|x|", "="]
]

## Frame to contain the button grid
#  Pack buttons so they fill out the frame
button_frame = Frame(window, bg="#a68d8d")
button_frame.pack(expand=True, fill="both", padx=8, pady=8)

## Configure the rows and columns of the button grid to expand equally
for i in range(len(buttons)):
    button_frame.grid_rowconfigure(i, weight=1, uniform="equal")

for i in range(max(len(row) for row in buttons)):
    button_frame.grid_columnconfigure(i, weight=1, uniform="equal")

## @brief Handle keyboard key presses
#  @param event The event object from tkinter
#
#  This maps keyboard keys to calculator input

def keypress_handler(event):
    key = event.char
    special = event.keysym
    if key in "0123456789+-*/%^=.":
        update_input(key)
    elif key == "\r":  # Enter
        update_input("=")
    elif key.lower() == "c":
        update_input("C")
    elif key == "\x08" or special == "BackSpace":  # Backspace
        update_input("⌫")
    elif key == "|":
        update_input("|x|")
    elif key == "!":
        update_input("!")
    elif key == "^":
        update_input("^")
    elif key == "√":
        update_input("√")


## Bind the keyboard input to the calculator
window.bind("<Key>", keypress_handler)

## @brief Format number based on magnitude: integer, float, or scientific.
#  @param n The number to format
#  @return Integer if whole number, otherwise rounded float

def format_number(n):
    """Format number based on magnitude: integer, float, or scientific."""
    if abs(n) >= 1e10 or (abs(n) < 1e-4 and n != 0):
        return "{:.6e}".format(n)
    elif float(n).is_integer():
        return int(n)
    else:
        return round(n, 8)


## @brief Show error in popup message window
#  @param message Error message to display

## @brief Show error in popup message window and flash whole window background red
#  @param message Error message to display
def show_error(message):
    original_color = "#a68d8d"
    error_color = "red"
    button_frame.config(bg=error_color)


    window.after(300, reset_background)
    messagebox.showerror("Calculation Error", message)



## @brief Resets the window background to normal after error flash
def reset_background():
    normal_bg = "#a68d8d"
    button_frame.config(bg=normal_bg)



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
#
#  This function routes each button press to the appropriate handler depending on the type:
#  - Digits are added to the input string
#  - Operators are saved for later evaluation
#  - '=' triggers computation
#  - Utility buttons like 'C', '⌫', '|x|' and '!' trigger their own logic
#  If the last action was '=', pressing any new button clears the state to start a fresh calculation.

def update_input(value):
    global just_evaluated

    if just_evaluated and (value.isdigit() or value == "."):
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
    elif value == "?":
        show_help()
    elif value.isdigit() or value == "." or (value == "-" and (not current_input or current_input == "-")):
        handle_digit(value)

    input_label.config(text=current_input if current_input else "0")
    just_evaluated = False  # Always reset this after any input except "="


## @brief Appends digit or sign to current input string
#  @param digit The string representing the digit (0–9) or negative sign ('-')
#
#  Builds up the number the user is typing. Called each time the user clicks a digit.
# Allow toggling minus sign at the beginning
def handle_digit(digit):
    global current_input

    if digit == ".":
        if "." not in current_input:
            if not current_input or current_input == "-":
                current_input += "0"  # If dot is first, prepend 0
            current_input += "."
    elif digit == "-" and current_input == "-":
        current_input = ""
    else:
        current_input += digit


## @brief Handles operator button press and stores operand/operator
#  @param op Operator character pressed
#
#  Evaluates any existing operation if operand and operator are already set,
#  then stores result as new operand and prepares for next input.
#  Also supports using '-' to type negative numbers.
# If the user is entering a negative number, allow '-' to be part of input
# If "-" pressed and typing a new negative number
# If operator already set but no second number typed, replace operator

def handle_operator(op):
    global current_input, operand, current_operator, history_input, just_evaluated

   
    if op == "-" and (not current_input or current_input == "-"):
        handle_digit("-")
        return

    if current_operator and not current_input:
        current_operator = op
        if operand is not None:
            history_input = f"{format_number(operand)}{op}"
            history_label.config(text=history_input)
        return

    if operand is not None and current_operator and current_input:
        handle_equal(chain=True)

    if current_input:
        operand = float(current_input)
        current_input = ""

    current_operator = op
    history_input = f"{format_number(operand)}{op}"
    history_label.config(text=history_input)
    input_label.config(text="0")
    just_evaluated = False


## @brief Executes the stored operation and updates the result
#  @param chain True if part of a chained operation
#  @return Displays result or error message
#
#  Based on the stored operator and the current input, this function performs the corresponding math operation using math_lib. 
#  It formats the result and updates both the history and input labels accordingly
#  It also handles chaining if another operator follows right after evaluation.

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
                result = math_lib.n_power(operand, second)
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
        show_error(str(e))
        clear_all()

## @brief Handles absolute value operation (|x|)
#  @return Updates input label with absolute value
#
#  Calls math_lib.absolute() and replaces current_input with the result.
#  Used for |x| button.

def handle_abs():
    global current_input, just_evaluated
    try:
        if operand is not None and current_operator and current_input:
            handle_equal()

        if current_input:
            result = format_number(math_lib.absolute(float(current_input)))
            current_input = str(result)
            input_label.config(text=current_input)
            just_evaluated = True
    except Exception as e:
        input_label.config(text="Error")
        show_error(str(e))
        clear_all()

## @brief Handles factorial operation (!)
#  @return Updates input label with factorial result
#
#  Converts current_input to int and uses math_lib.factorial().
#  Shows error if the number is negative or not an integer.

def handle_fact():
    global current_input, just_evaluated
    try:
        if operand is not None and current_operator and current_input:
            handle_equal()

        if current_input:
            value = float(current_input)
            if not value.is_integer():
                raise ValueError("Factorial only defined for integers")
            result = math_lib.factorial(int(value))
            current_input = str(format_number(result))
            input_label.config(text=current_input)
            just_evaluated = True
    except Exception as e:
        input_label.config(text="Error")
        show_error(str(e))
        clear_all()

## @brief Function to show the help message in a custom popup window
def show_help():
    help_message = (
        "🧮 Calculator Help Guide\n\n"
        
        "🔹 **Basic Controls**\n"
        "  • C     – Clear all input and reset state\n"
        "  • ⌫     – Delete the last character\n"
        "  • =     – Evaluate the current expression\n"
        "  • .     – Decimal point\n"
        "  • |x|   – Absolute value of the number\n"
        "  • !     – Factorial (only non-negative integers)\n"
        "  • ?     – Show this help window\n\n"

        "🔹 **Binary Operations** (require two operands)\n"
        "  • +     – Addition\n"
        "  • -     – Subtraction\n"
        "  • *     – Multiplication\n"
        "  • /     – Division (raises error if divisor is 0)\n"
        "  • %     – Modulo (remainder of division)\n"
        "  • ^     – Exponentiation (x to the power of n)\n"
        "  • √     – n-th root (x-th root of a number)\n\n"

        "🔹 **Notes**\n"
        "  • Use '.' for decimal numbers.\n"
        "  • Results are shown in scientific notation for very large or small values.\n"
        "  • Negative bases with even roots will raise an error (no real result).\n"
        "  • Factorial is only defined for whole numbers ≥ 0.\n"
        "  • Press any digit or operator after '=' to start a new calculation.\n"
    )
    messagebox.showinfo("Calculator Help", help_message)


## Assign colors to individual buttons
number_color = "#b39e8d"
operand_color = "#ed842f"
special_1_color = "#c45252"
special_2_color = "#93d9d7"
button_colors = {
    "C": special_1_color,
    "⌫": special_1_color,
    "%": operand_color,
    "^": operand_color,
    "√": operand_color,
    "/": operand_color,
    "*": operand_color,
    "-": operand_color,
    "+": operand_color,
    "=": special_2_color,
    "!": operand_color,
    "|x|": special_2_color,
    ".": special_2_color,
    "0": number_color,
    "1": number_color,
    "2": number_color,
    "3": number_color,
    "4": number_color,
    "5": number_color,
    "6": number_color,
    "7": number_color,
    "8": number_color,
    "9": number_color,
    "?": special_1_color
}

## @brief Create and place calculator buttons
# Loop for button creation
# Creates buttons with their assigned colors, default color if not found
for row_index, row in enumerate(buttons):
    for col_index, label in enumerate(row):
        if not label:
            continue
        
        btn_color = button_colors.get(label, "#F9E0AE")

        btn = Button(
            button_frame,
            text=label,
            font=("Arial", 18),
            bg=btn_color,
            activebackground="#FFD180",
            relief=FLAT,
            bd=0,
            highlightthickness=0,
            padx=10, pady=10,
            command=lambda val=label: update_input(val)
        )

        btn.original_bg = btn_color

        if label == "=":
            btn.grid(row=row_index, column=col_index, columnspan=2, sticky="nsew", padx=2, pady=2)
        else:
            btn.grid(row=row_index, column=col_index, sticky="nsew", padx=2, pady=2)

        def on_enter(e):
            e.widget['background'] = '#FFD180'

        def on_leave(e):
            e.widget['background'] = e.widget.original_bg

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)


## @brief Initialize the label displays
history_label.config(text=history_input)
input_label.config(text="0")

## @brief Start the tkinter main event loop
window.mainloop()
