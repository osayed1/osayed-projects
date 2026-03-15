import re
import math

password = input("put your password\n")
def check_length(pw):
    if len(pw) >= 8:
        return True
    else:
        return False

def has_lowercase(pw):
    return 26 if re.search(r"[a-z]", pw) else 0

def has_uppercase(pw):
    return 26 if re.search(r"[A-Z]", pw) else 0

def has_numbers(pw):
    return 10 if re.search(r"\d", pw) else 0

def has_special(pw):
    return 32 if re.search(r"[!@#$%^&*?]", pw) else 0


N = has_lowercase(password) + has_uppercase(password) + has_numbers(password) + has_special(password)
L = len(password)

if N == 0:
    entropy = 0
else:
    entropy = L * math.log2(N)

seconds = (2 ** entropy) / 10_000_000_000

minutes = seconds / 60
hours = minutes / 60
days = hours / 24
weeks = days / 7
months = days / 30

print("\nPassword Analysis Report")
print("------------------------")
print("Length >= 8      :", "✅" if check_length(password) else "❌")
print("Lowercase letters:", "✅" if has_lowercase(password) else "❌")
print("Uppercase letters:", "✅" if has_uppercase(password) else "❌")
print("Numbers          :", "✅" if has_numbers(password) else "❌")
print("Special chars    :", "✅" if has_special(password) else "❌")
print(f"Entropy          : {entropy:.3f} bits")
print(f"the time well takes you to breack the password : {days:.3f}")

if entropy <= 30:
    strength = "Weak password"
elif entropy <= 50:
    strength = "Good password"
elif entropy <= 70:
    strength = "Strong password"
else:
    strength = "So Strong Password"

print("Strength         :", strength)   
