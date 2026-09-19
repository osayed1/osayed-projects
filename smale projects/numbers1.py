big_num = int(input("pick a big number : "))
small_num = int(input("pick a small number : "))
for a in range(small_num, big_num + 1) :
    if a % 3 == 0 :
        continue
    if a == 20 :
        break
    if a ==big_num :
        break
    if a == 7 or a ==13 :
        print("spicle num btw")
    print(a)