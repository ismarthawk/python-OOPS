
class Player : 
	def __init__(self, name : str, age : int) : 
		self.name = name
		self.age = age
		self.runs = 0

	def getInfo(self) : 
		print("Name : " , self.name,"\nAge : ", self.age, "\nRuns : ", self.runs)

	def takeRun(self) : 
		self.runs += 1

p = Player('Damodar', 22)
p.getInfo()
p.takeRun()
print("\nAfter taking runs \n")
p.getInfo()


print(p)
print(type(p))