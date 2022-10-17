class Person : 
	def __init__(self, name : str, age : int) -> None : 
		self.name = name
		self.age = age

	def speak(self) -> None : 
		print(f"My name is {self.name} and I am {self.age} years old.")

p = Person("Damodar", 20)
p.speak()


# p.speak = "A method need to be implemented"
# p.speak()

# _ to denote private variables

class PrivatePerson : 
	def __init__(self, name, age) : 
		self._name = name
		self._age = age

	def _speak(self) : 
		print("My name is", self._name, " and I am ", self._age , "years old")
p = PrivatePerson("Naidu", 200)
p._speak()