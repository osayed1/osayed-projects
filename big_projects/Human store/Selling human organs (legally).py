
import json

from faker import Faker
fake = Faker()

with open("C:\\idk\\Human store\\log ins.txt") as afile:
     file = afile.read()

cost = {"eyes":2400,"heart":15000,"liver":3000}
with open("C:\\idk\\Human store\\human_organs_file.txt", "r") as f:
    human_organs = json.load(f)

class the_store :
    #chose = int(input("welcome to the human store\n chose what you want\n1-tech support\n2-cart\np3-roduct "))
    def __init__(self):
        pass
    def show_products(self):

        print(human_organs)
        print(cost)

    def cart(self):
        print("the cart is not working\n\n")
        self.menue()

    def buy(self):

        a = str(input(f"select your organe\n{human_organs}\n{cost}\nby typing the organe name\n"))

        if a == "eyes":

            eyes_num = int(input("how muny\n"))
            costing = eyes_num * cost["eyes"]
            desion = str(input(f"that well cost you {costing}$ riyale\n wana buy it ?\ntype yes or no \n"))
            if desion == "yes":
                money = int(input("put the money: "))

                if money == costing :
                    print("thx for useing ur program the packages well be in your house about 15 days")
                    human_organs["eyes"] -= eyes_num

                    with open("C:\\idk\\Human store\\human_organs_file.txt", "w") as f:
                        json.dump(human_organs, f)

                    self.menue()

                elif money >= costing :
                    print("thx for useing ur program the packages well be in your house about 7 days and thx for the tip \n also we well send you cobons in you email")
                    human_organs["eyes"] -= eyes_num 

                    with open("C:\\idk\\Human store\\human_organs_file.txt", "w") as f:
                        json.dump(human_organs, f)

                    self.menue()

                elif money <= costing:

                    print(f"no enoghe cash Mr {self.email_input}")
                    self.buy()

                else:
                    print("error")
                    self.first_things()
                    
            elif desion == "no":
                self.buy()

            else:
                print("error")
                self.first_things()

            if eyes_num > human_organs["eyes"]:
                    print("error")
            #else:
                #None
            else:
                print("Error")

        elif a == "liver":
            liver_num = int(input("how muny\n"))
            costing = liver_num * cost["liver"]
            desion = str(input(f"that well cost you {costing}$ riyale\n wana buy it ?\ntype yes or no \n"))

            if desion == "yes":
                money = int(input("put the money: "))

                if money == costing :
                    print("thx for useing ur program the packages well be in your house about 15 days")
                    human_organs["liver"] -= liver_num

                    with open("C:\\idk\\Human store\\human_organs_file.txt", "w") as f:
                        json.dump(human_organs, f)

                    self.menue()

                elif money >= costing :
                    print("thx for useing ur program the packages well be in your house about 7 days and thx for the tip \n also we well send you cobons in you email")
                    human_organs["liver"] -= liver_num

                    with open("C:\\idk\\Human store\\human_organs_file.txt", "w") as f:
                        json.dump(human_organs, f)

                    self.menue()

                elif money <= costing:
                    print(f"no enoghe cash Mr {self.email_input}")
                    self.buy()

                else:
                    print("error")
                    self.first_things()
                    
            elif desion == "no":
                self.buy()

            else:
                print("error")
                self.first_things()

            if liver_num > human_organs["liver"]:
                    print("error")
            #else:
                #None
                 
        elif a == "heart":
            heart_num = int(input("how muny\n"))
            costing = heart_num * cost["heart"]
            desion = str(input(f"that well cost you {costing}$ riyale\n wana buy it ?\ntype yes or no \n"))

            if desion == "yes":
                money = int(input("put the money: "))

                if money == costing :
                    print("thx for useing ur program the packages well be in your house about 15 days")
                    human_organs["heart"] -= heart_num

                    with open("C:\\idk\\Human store\\human_organs_file.txt", "w") as f:
                        json.dump(human_organs, f)

                    self.menue()

                elif money >= costing :
                    print("thx for useing ur program the packages well be in your house about 7 days and thx for the tip \n also we well send you cobons in you email")
                    human_organs["heart"] -= heart_num

                    with open("C:\\idk\\Human store\\human_organs_file.txt", "w") as f:
                        json.dump(human_organs, f)

                    self.menue()

                elif money <= costing:
                    print(f"no enoghe cash Mr {self.email_input}")
                    self.buy()

                else:
                    print("error")
                    self.first_things()
                    
            elif desion == "no":
                self.buy()

            else:
                print("error")
                self.first_things()

            if heart_num > human_organs["heart"]:
                    print("error")
            #else:
                #None
        else:
            print("Error")
        
    def first_things(self):

        first_thing = int(input(
            "welcome to HUMAN organs\n"
            "1-log in\n"
            "2-sign in\n"
            "3-exit\n"
        ))

        if first_thing == 1:

            email_input = input("put your email:\n")
            password_input = input("put your password:\n")

            with open("C:\\idk\\Human store\\log ins.txt") as afile:
                file = afile.read()

            self.login_account = email_input + ":" + password_input

            if self.login_account in file:
                print("login successful")
                self.email_input = email_input   # نحفظ الإيميل
                self.menue()
            else:
                print("email or password is wrong")

        elif first_thing == 2:
            new_email = input("put your email:\n")
            new_password = input("put your password:\n")

            self.account = new_email + ":" + new_password + "\n"

            with open("C:\\idk\\Human store\\log ins.txt", "a") as f:
                f.write(self.account)

            print("account created successfully, reopen the program")

        elif first_thing == 3:
            raise SystemExit
  
    def tech_support(self):

        problome = input("what is your problome:\n")
        filess = self.login_account + ": " + problome + "\n"

        with open ("C:\\idk\\Human store\\tech_support.txt", "a") as ff:
            ff.write(filess)
            
        print("thx for useing ur program thos well takes about 7-10 days or you can call us on +966569113682")
        self.menue()
    def menue(self):

        print(f"hallo {self.email_input}")
        self.chose = int(input("welcome to the human store\n chose what you want\n1-tech support\n2-cart\n3-product\n4-buy\n5-exit\n"))

        if self.chose == 1:
            self.tech_support()

        elif self.chose == 3:

            self.show_products()
            a =int(input("\n1-return\n"))

            if a == 1 :
                self.menue()
            else:
                print("error")
        elif self.chose == 2 :
            self.cart()
        elif self.chose == 4 :
            self.buy()
        elif self.chose == 5 :
            self.first_things()
        else:
            print("error")

store = the_store()
store.first_things()