
class student():

    def  __init__(self , name , age , dgree):
        self.name = name
        self.age = age 
        self.dgree = dgree

    def everything(self):
        print(f"the name is {self.name} and the age is {self.age} and the dgree is {self.dgree} ")
    def dgreeCH(self ,new_dgree):
        self.dgree = new_dgree

    def dgrees(self):
        if self.dgree >= 60 :
            print("you won")
        else:
            print("you are losser")

a = student("ahmad" , 15 , 80)
a.dgreeCH(30)
a.everything()
a.dgrees()
        