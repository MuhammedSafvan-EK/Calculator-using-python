from tkinter import *

window=Tk()       #create window
window.title("Calculator")   #window bar title
window.geometry("500x500")   #size of the window

# Create a Frame for the calculator
calc_frame=Frame(window,bd=5,relief=RIDGE,padx=10,pady=10)
calc_frame.pack(pady=50)


# Configure grid columns  to allow centering
# total_columns=4
# for col in range(total_columns):    #col is a loop variable it represent current column index initially col is zero
#     calc_frame.grid_columnconfigure(col,weight=1) #weight=1 gives all columns equal "expanding power".

# Entry for input (Text is for multiline; Entry is better for calculators)
entry=Entry(calc_frame,width=50,justify='right')                                           #entry can be used to single line text input,text - multiple line
entry.grid(row=0,column=0,columnspan=4,pady=(20,30))   #align,justify='right' means:It aligns the text inside the Entry box to the right side as you type.


# Button functions
def seven():                        #It inserts the number 7 into the Entry widget when the function is called — usually by clicking the 7 button on your calculator.
    entry.insert(END,"7")    #A special Tkinter constant that means "add to the end" of current text.

def eight():
    entry.insert(END,"8")

def nine():
    entry.insert(END,"9")

def division():
    entry.insert(END, "/")

def four():
    entry.insert(END, "4")

def five():
    entry.insert(END, "5")

def six():
    entry.insert(END, "6")

def mul():
    entry.insert(END, "*")

def one():
    entry.insert(END, "1")

def two():
    entry.insert(END, "2")

def three():
    entry.insert(END, "3")

def sub():
    entry.insert(END, "-")

def zero():
    entry.insert(END,"0")

def dot():
    entry.insert(END, ".")

def equal_to():
    entry.insert(END, "=")

def add():
    entry.insert(END,"+")

def clear():
    entry.delete(0,END) #(0) each digit can be removed ,(0,END) it can be used to delete whole numbers


# Buttons rows
seven_button=Button(calc_frame,text="7",width=10,height=2,command=seven)
seven_button.grid(row=1,column=0,padx=5,pady=5)

eight_button=Button(calc_frame,text="8",width=10,height=2,command=eight)
eight_button.grid(row=1,column=1,padx=5,pady=5)

nine_button=Button(calc_frame,text="9",width=10,height=2,command=nine)
nine_button.grid(row=1,column=2,padx=5,pady=5)

div_button=Button(calc_frame,text="/",width=10,height=2,command=division)
div_button.grid(row=1,column=3,padx=5,pady=5)

four_button=Button(calc_frame,text="4",width=10,height=2,command=four)
four_button.grid(row=2,column=0,padx=5,pady=5)

five_button=Button(calc_frame,text="5",width=10,height=2,command=five)
five_button.grid(row=2,column=1,padx=5,pady=5)

six_button=Button(calc_frame,text="6",width=10,height=2,command=six)
six_button.grid(row=2,column=2,padx=5,pady=5)

mul_button=Button(calc_frame,text="*",width=10,height=2,command=mul)
mul_button.grid(row=2,column=3,padx=5,pady=5)

one_button=Button(calc_frame,text="1",width=10,height=2,command=one)
one_button.grid(row=3,column=0,padx=5,pady=5)

two_button=Button(calc_frame,text="2",width=10,height=2,command=two)
two_button.grid(row=3,column=1,padx=5,pady=5)

three_button=Button(calc_frame,text="3",width=10,height=2,command=three)
three_button.grid(row=3,column=2,padx=5,pady=5)

sub_button=Button(calc_frame,text="-",width=10,height=2,command=sub)
sub_button.grid(row=3,column=3,padx=5,pady=5)

zero_button=Button(calc_frame,text="0",width=10,height=2,command=zero)
zero_button.grid(row=4,column=0,padx=5,pady=5)

dot_button=Button(calc_frame,text=".",width=10,height=2,command=dot)
dot_button.grid(row=4,column=1,padx=5,pady=5)

equal_to_button=Button(calc_frame,text="=",width=10,height=2,command=equal_to)
equal_to_button.grid(row=4,column=2,padx=5,pady=5)

add_button=Button(calc_frame,text="+",width=10,height=2,command=add)
add_button.grid(row=4,column=3,padx=5,pady=5)

clear_button=Button(calc_frame,text="Clear",width=10,height=2,command=clear)
clear_button.grid(row=4,column=4,padx=5,pady=5)





window.mainloop()