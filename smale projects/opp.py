
class Vehicle:
    def __init__(self, size, color):
        self.price = 0
        self.size = size
        self.color = color

    def colorr(self):
        self.color_p = 0
        self.black_p = 200
        self.wihte_p = 300

        if self.color == "black":
            self.price = self.black_p
            self.color_p = self.black_p

        elif self.color == "wihte":
            self.price = self.wihte_p
            self.color_p = self.wihte_p

        else:
            raise ValueError(f"{self.color} not avaliable, you can onlay use wihte or black")
        return f"this cost : ${self.color_p}"

class Car(Vehicle):
    cars = 0
    def __init__(self, size, model, color, maxspeed, gasoline, carage):
        super().__init__(size, color)
        self.model = model
        self.maxspeed = maxspeed
        self.gasoline = gasoline
        self.carage = carage
        self.cars += 1

    def sizze(self):
        self.big = 30000
        self.meduime = 20000
        self.small = 10000
        size_p = 0

        if self.size == "big":
            self.price = self.big
            size_p = self.big

        elif self.size == "meduime":
            self.price = self.meduime
            size_p = self.meduime

        elif self.size == "small":
            self.price = self.small
            size_p = self.small

        else:
            raise ValueError (f"{self.size} not avaliable, you can only use big, meduime, small")
        return f"that will cost : ${size_p}"
    
class Bike(Vehicle):
    pass        
    
my_car = Car("big" , "GMC", "black", "200", "red", "2000")
my_car2 = Car("small", "GMC", "wihte", "200", "red", "2000")
#print(car1.sizze() + car1.colorr() + f" this will cost myfrind {car1.price}")
#print(car2.sizze() + car2.colorr() + f"that will be {car2.price}")
my_bike = Bike("big", "wihte")

print(my_car.colorr())
print(my_car2.colorr())
print(my_bike.colorr())
