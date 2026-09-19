
import tkinter as tk

mom = tk.Tk()
mom.title("the program")
mom.geometry("600x600")

mom1 = tk.Label( mom ,text ="halo to this program" )
mom1.grid(padx=250)

entry = tk.Entry(mom)
entry.grid()

def show_txt() :
    lol = entry.get()
    mom1.config(text=lol , fg="red")

botten = tk.Button(mom , text="show text" , command=show_txt)
botten.grid()


mom.mainloop()