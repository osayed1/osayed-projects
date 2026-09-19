age = int(input("your age "))
expirince = int(input("years expirince:"))
edu = str(input("your edu:"))
if age>=20 and age<=35:
    if expirince>=1:
        if edu in ["master", "bachelor", "diploma"]:
            print("you are accepted")
        else:
            print("your edu is low")
            print("you didnt get the accept\n try another time")
    else:
        print("your expirince years is low")
        print("you didnt get the accept\n try another time")
else:
    print("your age is not exepteble")
    print("you didnt get the accept\n try another time")