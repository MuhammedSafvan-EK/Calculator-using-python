from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("500x500")

# Create a Frame for the calculator
calc_frame = Frame(window, bd=5, relief=RIDGE, padx=10, pady=10)
calc_frame.pack(pady=50)

# Entry for input (Text is for multiline; Entry is better for calculators)
entry = Entry(calc_frame, width=50, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=(20, 30))

# Global variables to store operation state
first_number = None
operator = None

# Handle number and dot input
def button_click(value):        #function with parametre
    entry.insert(END, value)  #This function handles input from number buttons (0–9) and the dot (.) button in your calculator
                              #END is a special Tkinter constant, which means:Insert the value at the end of the current text

# Handle operator button
def set_operator(op):       #it takes op as a parameter, which will be a string like "+", "-", "*", or "/" — depending on which operator button the user clicks
    global first_number, operator  #declare global var
    try:
        first_number = float(entry.get()) #Reads the current number from the Entry widget (user’s first input)
        operator = op
        entry.delete(0, END)  ##Clears the input box (so the user can now type the second number)
    except:  #the Entry has no valid number
        entry.delete(0, END)    #(0) each digit can be removed ,(0,END) it can be used to delete whole numbers
        entry.insert(END, "Error")

# Perform the operation when '=' is clicked
def equal_to():
    global first_number, operator
    try:
        second_number = float(entry.get())  #get second number into input
        result = 0
        if operator == '+':
            result = first_number + second_number
        elif operator == '-':
            result = first_number - second_number
        elif operator == '*':
            result = first_number * second_number
        elif operator == '/':
            if second_number == 0:
                raise ZeroDivisionError #move to except
            result = first_number / second_number
        entry.delete(0, END)
        entry.insert(END, str(result))
    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(END, "Cannot divide by 0")
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Clear button
def clear():
    global first_number, operator
    entry.delete(0, END)
    first_number = None
    operator = None

# Button layout: numbers and operators ,list of tuples peach tuple contain three element
#syntax= each tuple(label(button label), row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

#for (text, row, col) in buttons:
# This line loops through each tuple in the buttons list.
# Each tuple contains:
#       text: the button label (e.g., '7', '+', '=')
#       row: the grid row number
#       col: the grid column number

for (text, row, col) in buttons:
    if text in '0123456789.':
        # If the button is a digit or dot, assign an action that calls button_click() with the button's value.
        action = lambda x=text: button_click(x)
    elif text in '+-*/':
        action = lambda x=text: set_operator(x) #if it's an operator (+, -, *, /), the button will call set_operator() with the symbol.
    elif text == '=':
        action = equal_to
    Button(calc_frame, text=text, width=10, height=2, command=action).grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = Button(calc_frame, text="Clear", width=50, height=2, command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

window.mainloop()
