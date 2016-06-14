class Person (object):
	def __init__(self,name):
		self.name=name
	def sayHello(self):
		print("Hi "+self.name)
		print("Hi ",self.name)
	

person=Person("Collin")
person.sayHello()
