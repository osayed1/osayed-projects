age = int(input("your age :"))
sessions = int(input("how muny session you can take :"))
fitness = str(input("your fitness leavel :"))
if age>=18 and age<=50 :
    if sessions>=3 :
        if fitness in ["high","medium"]:
             print("you are accepted")
        else:
            print("rejected: your age does not meet the requirement")
            print("you didnt get the accept\n try another time")
    else:   
        print("rejected: not enough weekly sessions")
        print("you didnt get the accept\n try another time")
else:
        print("rejected: your fitness level is too low")
        print("you didnt get the accept\n try another time")