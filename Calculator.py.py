import math
from tkinter import *
Str= ""

def percent():
    num=int(e_field.get())
    result=num/100
    e_field.delete(0,END)
    e_field.insert(END,result)

def root():
    num = float(e_field.get())
    result = math.sqrt(num)
    e_field.delete(0, END)
    e_field.insert(END, result)
def fact():
    num = int(e_field.get())
    result = math.factorial(num)
    e_field .delete(0, END)
    e_field.insert(END, result)

def click(num):
    global Str
    Str = Str + str(num)
    e.set(Str)
 
def equal():
    try:
        global Str
        total = str(eval(Str))
        e.set(total)
        Str= ""
    except:
        e.set(" error ")
        Str = ""

def clear():
    global Str
    Str = ""
    e.set("")

if __name__=='__main__':
    screen= Tk()
    screen.title("CALCULATOR")
    screen.geometry("236x340")
    e = StringVar()
    e_field = Entry(screen, textvariable=e)
    e_field.grid(columnspan=100, ipadx=53,ipady=20)

    one = Button(screen, text=' 1 ',
                    command=lambda: click(1),bg="gray80", height=3, width=7)
    one.grid(row=2, column=0)
 
    two = Button(screen, text=' 2 ', 
                    command=lambda: click(2),bg="gray80", height=3, width=7)
    two.grid(row=2, column=1)
 
    three = Button(screen, text=' 3 ',
                    command=lambda: click(3),bg="gray80", height=3, width=7)
    three.grid(row=2, column=2)
 
    four = Button(screen, text=' 4 ',
                    command=lambda: click(4),bg="gray80",height=3, width=7)
    four.grid(row=3, column=0)
 
    five = Button(screen, text=' 5 ', 
                    command=lambda: click(5),bg="gray80", height=3, width=7)
    five.grid(row=3, column=1)
 
    six = Button(screen, text=' 6 ', 
                    command=lambda: click(6),bg="gray80", height=3, width=7)
    six.grid(row=3, column=2)
 
    seven = Button(screen, text=' 7 ', 
                    command=lambda: click(7),bg="gray80", height=3, width=7)
    seven.grid(row=4, column=0)
 
    eight = Button(screen, text=' 8 ', 
                    command=lambda: click(8),bg="gray80", height=3, width=7)
    eight.grid(row=4, column=1)
 
    nine = Button(screen, text=' 9 ', 
                    command=lambda: click(9),bg="gray80", height=3, width=7)
    nine.grid(row=4, column=2)
 
    zero = Button(screen, text=' 0 ', 
                    command=lambda: click(0),bg="gray80", height=3, width=7)
    zero.grid(row=5, column=1)

    plus = Button(screen, text=' + ',
    command=lambda: click("+"),bg="gray59", height=3, width=7)
    plus.grid(row=2, column=3)
    minus = Button(screen, text=' - ', 
                command=lambda: click("-"),bg="gray59", height=3, width=7)
    minus.grid(row=3, column=3)
    multiply = Button(screen, text=' * ',
                    command=lambda: click("*"),bg="gray59", height=3, width=7)
    multiply.grid(row=4, column=3)
    divide = Button(screen, text=' / ', 
                    command=lambda: click("/"),bg="gray59", height=3, width=7)
    divide.grid(row=5, column=3)
    Decimal= Button(screen, text='.', 
                    command=lambda: click('.'),bg="gray59", height=3, width=7)
    Decimal.grid(row=5, column=2)
    clear = Button(screen, text='Clear',bg="red",
                command=clear, height=3, width=7)
    clear.grid(row=8, column=3)
    equal = Button(screen, text=' = ', 
                command=equal,bg="light sky blue",height=3, width=7)
    equal.grid(row=8,column=2)
    Root = Button(screen, text="√",bg="gray59", height=3,width=7,command=root)
    Root.grid(row=8,column=0)
    Fact =Button(screen, text="!",bg="gray59", height=3,width=7,command=fact)
    Fact.grid(row=5,column=0)
    
    Percent=Button(screen,text="%",command=percent,bg="gray59",height=3,width=7)
    Percent.grid(row=8,column=1)
    
    screen.mainloop()