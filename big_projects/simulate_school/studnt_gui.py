
import tkinter as tk
#this project so fucking hard i hate this shit
import ast

with open ("C:\\idk\\student_project\\students") as file:
    read_file = file.read()
    file.seek(0)
appndfile = open ("C:\\idk\\student_project\\students", "r+") 

prog_name = "student"

display = tk.Tk()
display.geometry("600x600")
display.title(prog_name)

entry = tk.Entry(display, width=20)
entry.grid(padx=250, pady=10,row=1, column=0)

class student:

    def __init__(self):
        #self.name_age = [
            #("mohhamad", 14),("ahmad", 13),("khaled",16),("zayed",15)
        #]

        self.appndfile2 = appndfile
        self.read = read_file

    def show_everything(self):
         
        with open("C:\\idk\\student_project\\students", "r") as f:
            data = f.read()

        for widget in display.grid_slaves(row=9, column=0):
            widget.destroy()

        lab = tk.Label(display, text=data)
        lab.grid(row=9, column=0)

        #lab = tk.Label(display, text=self.name_age)

    def put_student(self):

        lable = tk.Label(display, text="name added seccessfully!")
        lable.grid(row=0, column=0)

        name = entry.get().strip()
        if not name:
            return

        with open("C:\\idk\\student_project\\students", "r") as f:
            data = f.read().strip()

        if data:
            data += f",({name})"
        else:
            data = f"({name})"

        with open("C:\\idk\\student_project\\students", "w") as f:
            f.write(data)

        self.read = data

        entry.delete(0, tk.END)


    def end_the_list(self) :

        ennd = open("C:\\idk\\student_project\\students", "a") 
        ennd.write("]")

        self.read += "]"

    def remove_the_endlist(self):

        with open("C:\\idk\\student_project\\students", "r") as file:
            data = file.read()

    
        data = data.replace("]", "")

        with open("C:\\idk\\student_project\\students", "w") as file:
            file.write(data)

        self.read = self.read.replace("]", "")

    def remove_student(self):
        name = entry.get().strip()
        if not name:
            return

        with open("C:\\idk\\student_project\\students", "r") as file:
            data = file.read()

        target = f"(,{name})"
        if target not in data:
            lable = tk.Label(display, text="name not found")
            lable.grid(row=0, column=0)
            return

        data = data.replace(target, "")

        with open("C:\\idk\\student_project\\students", "w") as file:
            file.write(data)

        self.read = data

        entry.delete(0, tk.END)

    def serch_for_student(self):
        
        index = entry.get().strip()

        with open("C:\\idk\\student_project\\students", "r") as f:
            data = f.read()

        students_list = ast.literal_eval(data)

        if 0 <= index < len(students_list):
            lab = tk.Label(display, text=students_list)
            lab.grid(row=9, column=0)

        else:
            lable = tk.Label(display, text="eror index")
            lable.grid(row=0, column=0)
            return
        
    def student_dgree(self):
        None

    
stu = student()


but1 = tk.Button(display, text="add new student", command=stu.put_student)
but1.grid(padx=50, pady=20)

but2 = tk.Button(display, text="remove student", command=stu.remove_student)
but2.grid(padx=50, pady=20)

but3 = tk.Button(display, text="show all students",command=stu.show_everything)
but3.grid(padx=50, pady=20)

but6 = tk.Button(display, text="end the list", command= stu.end_the_list)
but6.grid(padx=50, pady=20)

but7 = tk.Button(display, text="remove]", command= stu.remove_the_endlist)
but7.grid(padx=50, pady=20)

display.mainloop()