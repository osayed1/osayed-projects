ch = int(input("1=all the planes\n2=appned a plane\n3=quite : "))
with open("C:\\Users\\osayed\\Desktop\\New folder (2)\\tasks.txt" , "r") as file:
    read = file.read()
    file = file
afile = open("C:\\Users\\osayed\\Desktop\\New folder (2)\\tasks.txt" , "a")   
if ch == 1 :
    print(read)    
elif ch == 2 :
    lol = input(" put the new plane :\n")
    afile.write(lol)
elif ch == 3 :
    print("Goodbay!")
else:
    print("error")
file.close()
afile.close()