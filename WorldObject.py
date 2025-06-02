class WorldObject:
	# ID = double, invetory = array
	def __init__(self, ID, inventory):
		self.ID = ID
		self.inventory = inventory

	def getID(self):
		return self.ID

	def showInventory(self):
		return self.inventory

	# call method if you need to create the same object with a different inventory
	def createUnique(self, diffInventory):
		return WorldObject(self.ID, diffInventory)