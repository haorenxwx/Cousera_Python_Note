pythonStructuredTemplate.py

========
class
========
class PartyAnimal:
	x = 0

	def __init__(self):
		print('I am the constructed')
	def party(self):
		self.x = self.x+1
		print('So far', self.x)
	def __del__(self):
		print('I am destructed', self.x)
an = PartyAnimal()
an.party()
an = 42
print('an contains',an)

========
Inheritance
========

class FootballFan(PartyAnimal):
	points = 0
	def touchtown(self):
		self.points +=7
		self.party()
		print(self.name,"points",self.points)
