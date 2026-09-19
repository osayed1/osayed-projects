
age = 16
def cheke_age(func):
    def age_wrapper():
        allow_age = 13

        if age >= allow_age:
            func()
        else:
            print(f"you must turn 18")
    return age_wrapper

@cheke_age
def print_age():
    print("this is you age")

print_age()