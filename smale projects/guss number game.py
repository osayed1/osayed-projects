
import random
num1 = random.randint(1,10)
num2 = random.randint(1,50)
num3 = random.randint(1,100)
f1_time = 5
f2_time =7
f3_time = 10
print("today we are going to play 'guss the number' game")
ass = int(input("1-ez\n2-medium\n3-hard"))
if ass == 1 :
    while f1_time>0 :
        a1 = int(input("pick a number betwen 1-10 :"))
    
        if a1 == num1 :
            print("wp")
            break
        else :
            f1_time-=1
            print("try again")
    if f1_time == 0 :
        print(f"you lost the game the number was {num1}")
elif ass == 2 :
    while f2_time>0 :
        a2 = int(input("pick a number betwen 1-50 :"))
    
        if a2 == num2 :
            print("wp")
            break
        else :
            f2_time-=1
            print("try again")
    if f2_time == 0 :
        print(f"you lost the game the number was {num2}")

elif ass == 3 :
    while f3_time>0 :
        a3 = int(input("pick a number betwen 1-100 :"))
    
        if a3 == num3 :
            print("wp")
            break
        else :
            f3_time-=1
            print("try again")
    if f3_time == 0 :
        print(f"you lost the game the number was {num3}")
