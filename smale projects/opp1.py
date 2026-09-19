desion = int(input("if you chose 1 you will loss\nbut if you chose 2 you win\n"))
num = 0

def deco(func):
    def count():
        global num
        if desion == 2:
            num += 1
            func()
            print(f"num is = {num}")
        else:
            print("goodbay")
    return count


@deco
def ass():
    print("hi form sapce")

ass()
ass()
ass()