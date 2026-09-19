
def first (func):
    def my_decoretors():
        print("start")
        func()
        print("end")

    return my_decoretors

@first
def say_hallo ():
    print("hallo")

say_hallo()