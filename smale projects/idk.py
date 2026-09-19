from datetime import datetime

class Age:
	def __init__(self, name, year, month, day):
		self.name = name
		self.year = year
		self.month = month
		self.day = day

	def agecount(self):
		self.yearb = datetime.now().year - self.year
		self.monthb = datetime.now().month - self.month
		self.dayb = datetime.now().day - self.day
		self.absmounth = abs(self.monthb)
		self.age = [self.yearb, self.absmounth, self.dayb]
		return f"{self.name} your age is {self.age}"
	
human = Age("osayed",2008, 5, 22)
print(human.agecount())
#print(datetime.now())
