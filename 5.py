class Person: 
	def __init__(self) : 
		pass
	def greet(self) : 
		print("Hello I am a person")
		return 

class User(Person) : 
	def __init__(self, name, age, id) : 
		self._name = name
		self._age = age
		self._id = id

user = User("siddu", 20, "ABCD")
print(user)
user.greet()
person = Person()

print(isinstance(user, User))
print(isinstance(person, Person))
print(isinstance(person, User))
print(isinstance(user, Person))

#base class object

print(isinstance(person, object))
print(isinstance(user, object))