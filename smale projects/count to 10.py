num = int(input("pick a num: "))
i = num

while i < 10:
    i += 1

    if i % 3 == 0:
        continue

    print(i)

    if i == 10:
        print("we are done")
        break