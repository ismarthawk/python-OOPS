



class Person: 
	def __init__(self, email) : 
		self.emai = email
	def greet(self) : 
		print("Hello There !", end = " " )
		return 

class User(Person) : 
	def __init__(self, name, age, id, email) : 
		super().__init__( email)
		self._name = name
		self._age = age
		self._id = id


	def greet(self) :
		Person.greet(self) 
		print("Hello ! I am", self._name)

user = User("siddu", 20, "ABCD", "damodar.pulla@gmail.com")
print(user)
user.greet()
print(user.__dict__)
print(user.__str__())