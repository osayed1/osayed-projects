
from faker import Faker 
fake = Faker()

file = open ("C:\\idk\\Human store\\log ins.txt","a")

a = fake.name()+ " " + fake.email() + " " + fake.city()
#print(a)
fake_email = fake.email()
fake_password = fake.password()
account = fake_email + ":" + fake_password + "\n"

file.write(account)