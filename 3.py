
class Player : 

	# this is a class attribute
	tornyRunning = True
	def __init__(self, name : str, age : int) : 
		self.name = name
		self.age = age
		self.runs = 0

	@classmethod
	def createGreatPlayer(self, name : str, age : int, color : str) : 
		k = self(name, age)
		k.color = color
		return k

	def getInfo(self) : 
		print("Name : " , self.name,"\nAge : ", self.age, "\nRuns : ", self.runs)


	def takeRun(self) : 
		print(f'Runs taken in the torny is {Player.tornyRunning}')
		self.runs += 1

	@staticmethod
	def toggleTorny() : 
		Player.tornyRunning = not Player.tornyRunning




p1 = Player.createGreatPlayer('Damodar', 22, 'Black')
print(p1.__dict__)
p1.toggleTorny()
print(p1.tornyRunning)



# p.getInfo()
# p.takeRun()
# print("\nAfter taking runs \n")
# p.getInfo()


# print(p)
# print(type(p))

