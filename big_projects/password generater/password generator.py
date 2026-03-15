import random

letters = "abcdefghijklmnopqrstuvwxyz"
special_letters ="+=_-()*&^%$#@!`~?/>.<,\\|[]':"
numberss = "0123456789"

print("this program do password generator ")

small_l_num = int(input("how muny small letters you want ?\n"))
big_l_num = int(input("how muny big letters you want ?\n"))
l_num = int(input("how muny numbers you want ?\n"))
l_special_num = int(input("how muny special cha you want ?\n"))


def small_letters():
    result = ""
    for _ in range(small_l_num):
        result += random.choice(letters)
    return result

def big_letters():
    result = ""
    for _ in range(big_l_num):
        result += random.choice(letters.upper())
    return result

def numbers():
    result = ""
    for _ in range(l_num):
        result += random.choice(numberss)
    return result

def special():
    result = ""
    for _ in range(l_special_num):
        result += random.choice(special_letters)
    return result
    
password = small_letters() + big_letters() + numbers() + special()
print(f"your password: {password}")
