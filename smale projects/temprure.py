import math

a = int(input("choose what 1-temperature or 2-distance:\n"))

def temperature():
    choice = int(input("do you want transfer to 1-°C or to 2-fahrenheit:\n"))

    if choice == 1:
        number = float(input("put the number:\n"))
        cal1 = (number - 32) * 5 / 9
        print(cal1, "°C")

    elif choice == 2:
        number = float(input("put the number:\n"))
        cal2 = (9 / 5 * number) + 32
        print(cal2, "°F")

    else:
        print("Error")

def distance():
    choice = int(input("do you want transfer to 1-Km or 2-miles:\n"))

    if choice == 1:
        number = float(input("put the number:\n"))
        mile = number * 0.621371
        print(mile, "miles")

    elif choice == 2:
        number = float(input("put the number:\n"))
        km = number * 1.60934
        print(km, "km")

    else:
        print("Error")

if a == 1:
    temperature()
elif a == 2:
    distance()
else:
    print("Error")
