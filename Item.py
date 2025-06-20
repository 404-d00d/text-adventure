class Item:
	def __init__(self, ID, name, description, isStackable, quantity=1, maxQuantity=1):
		self.ID = ID
		self.name = name
		self.description = description
		self.isStackable = isStackable
		self.quantity = 1 if not isStackable else quantity
		self.maxQuantity = 1 if not isStackable else maxQuantity

	def getID(self):
		return self.ID

	def getName(self):
		return self.name

	def getDescription(self):
		return self.description

	def getQuantity(self):
		return self.quantity

	def createInstance(self):
		return "item"

class Key(Item):
	def __init__(self, ID, name, description, isStackable, DoorID, quantity=1, maxQuantity=1):
		self.ID = ID
		self.name = name
		self.description = description
		self.isStackable = isStackable
		self.DoorID = DoorID
		self.quantity = 1 if not isStackable else quantity
		self.maxQuantity = 1 if not isStackable else maxQuantity

	def getDoorID(self):
		return self.DoorID