
def positive_only(func):
    def wrapper(num):
        if num >= 0:
            func(num)
        else:
            print(f"you cant save this {num} sir")
    return wrapper

@ positive_only
def print_m(num):
    print(f"you have {num} money")

print_m(50)
print_m(-100)