import tkinter
from tkinter import PhotoImage

a = 1

gui = tkinter.Tk()
gui.title("calculator")
gui.geometry("600x600")
gui.config(background="#818181")
#icon = PhotoImage(file="C:\\Users\\osayed\\Desktop\\New folder (2)\\12.png")  
#gui.iconphoto(True, icon)


entry = tkinter.Entry(gui, width=30)
entry.grid(row=0, column=15, padx=300, pady=0)

def num (value):
    print(value, end="")
    current = entry.get()
    entry.delete(0, tkinter.END)
    entry.insert(0, current + str(value))

def a():
    expression = entry.get()  
    try:
        result = eval(expression)  
        entry.delete(0, tkinter.END)  
        entry.insert(0, str(result))  
    except:
        entry.delete(0, tkinter.END)
        entry.insert(0, "Error")  

def clear_cal () :
    entry.delete(0 , tkinter.END )



but1 = tkinter.Button(gui, text="1", command=lambda: num(1))
but1.grid(row=0, column=0, padx=10, pady=10)

but2 = tkinter.Button(gui, text="2", command=lambda: num(2))
but2.grid(row=0, column=1, padx=10, pady=10)

but3 = tkinter.Button(gui, text="3", command=lambda: num(3))
but3.grid(row=0, column=2, padx=10, pady=10)

but4 = tkinter.Button(gui, text="4", command=lambda: num(4))
but4.grid(row=1, column=0, padx=10, pady=10)

but5 = tkinter.Button(gui, text="5", command=lambda: num(5))
but5.grid(row=1, column=1, padx=10, pady=10)

but6 = tkinter.Button(gui, text="6", command=lambda: num(6))
but6.grid(row=1, column=2, padx=10, pady=10)

but7 = tkinter.Button(gui, text="7", command=lambda: num(7))
but7.grid(row=2, column=0, padx=10, pady=10)

but8 = tkinter.Button(gui, text="8", command=lambda: num(8))
but8.grid(row=2, column=1, padx=10, pady=10)

but9 = tkinter.Button(gui, text="9", command=lambda: num(9))
but9.grid(row=2, column=2, padx=10, pady=10)

but0 = tkinter.Button(gui, text="0", command=lambda: num(0))
but0.grid(row=3, column=1, padx=10, pady=10)



butx = tkinter.Button(gui, text="*", command=lambda: num('*'))
butx.grid(row=0, column=3, padx=10, pady=10)

butg = tkinter.Button(gui, text="/", command=lambda: num('/'))
butg.grid(row=0, column=4, padx=10, pady=10)

butPlus = tkinter.Button(gui, text="+", command=lambda: num('+'))
butPlus.grid(row=1, column=3, padx=10, pady=10)

butNig = tkinter.Button(gui, text="-", command=lambda: num('-'))
butNig.grid(row=1, column=4, padx=10, pady=10)


butE = tkinter.Button(gui, text="=", command=a)
butE.grid(row=1, column=4, padx=10, pady=10)

but_clear = tkinter.Button(gui , text="clear" , command=clear_cal)
but_clear.grid(row=3, column=4, padx=10, pady=10)


gui.mainloop()