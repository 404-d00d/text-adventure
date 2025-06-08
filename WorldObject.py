class WorldObject:
	# ID = double, invetory = array
	def __init__(self, ID, inventory, description, inspect, interaction):
		self.ID = ID
		self.inventory = inventory
		self.description = description
		self.inspect = inspect
		self.interaction = interaction
		self.options = ("-----\n"
					  "1. Look Closer\n"
					  "2. Interact\n"
					  "Any Other Option. Do Nothing")

	def getID(self):
		return self.ID

	def showInventory(self):
		return self.inventory

	def showDescription(self):
		return self.description

	def showOptions(self):
		return self.options

	# 1 = look closer
	# 2 = interact
	# anything else = do nothing
	def interact(self, response):
		if response == "1":
			return (self.inspect)
		elif response == "2":
			return (self.interaction)
		else:
			return ("You do nothing")

	# call method if you need to create the same object with a different inventory
	def createUnique(self, diffInventory):
		return WorldObject(self.ID, diffInventory, self.description, self.inspect, self.interaction)