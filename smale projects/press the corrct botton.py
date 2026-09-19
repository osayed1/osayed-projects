
import tkinter as tk
import random 
from random import randint 

game = tk.Tk()
game.title("game")
game.geometry("500x600")
game.config( bg="#9895ff")

rm = random.randint(1,3)

def pressed(number):
    if number == rm:
        ww = tk.Label(game , text="you won")
        ww.grid()
    else:
        w = tk.Label(game , text="you lost")
        w.grid()


first_num = tk.Button(game , text=1 , command=lambda : pressed(1))
second_num = tk.Button(game , text=2 , command=lambda : pressed(2))
therd_num = tk.Button(game , text=3, command=lambda : pressed(3))




first_num.grid(row=1, column=0 , padx=10 , pady=10)
second_num.grid(row=1, column=1 , padx=10 , pady=10)
therd_num.grid(row=1, column=2 , padx=10 , pady=10)



game.mainloop()