class Person (object):
	def __init__(self,name):
		self.name=name
	def sayHello(self):
		return "Hi "+self.name
		return "Hi ",self.name
	

person=Person("Collin")
person.sayHello()
