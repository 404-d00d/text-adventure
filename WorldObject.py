class WorldObject:
	# ID = double, invetory = array/dictionary
	def __init__(self, inventory, ID, description, inspect, interaction):
		self.inventory = inventory
		self.ID = ID
		self.description = description
		self.inspect = inspect
		self.interaction = interaction
		self.options = ("-----\n"
					  "1. Look Closer\n"
					  "2. Interact\n"
					  "3. Show Inventory\n"
					  "4. Add to Inventory\n"
					  "Any Other Option. Do Nothing")

	def getID(self):
		return self.ID

	def showInventory(self):
		print("===")
		print("OBJECT INVENTORY")
		for x in range(len(self.inventory)):
			print(str(x)+": "+str(self.inventory[x].getQuantity())+" "+self.inventory[x].getName())

	def lootInventory(self, player):
		selection = ""
		while selection != "e":
			try:
				self.showInventory()
				print("e: exit inventory")
				selection = input("Choose your option: ")
				selection = int(selection)
				print(self.inventory[selection].getName()+" is the item you selected.")
				player.addItem(self.inventory[selection])
				self.inventory.pop(selection)
			except (ValueError, IndexError):
				print("This option is not valid.")
		return ("You are done with this item")

	def placeIntoInventory(self, player):
		selection = ""
		while selection != "e":
			try:
				player.showInventory()
				print("e: exit inventory")
				selection = input("Choose your option: ")
				selection = int(selection)
				print(player.getInventory()[selection].getName()+" is the item you put into the object")
				self.inventory.append(player.showInventory()[selection])
				player.removeItem(self.inventory[selection])
			except (ValueError, IndexError):
				print("This option is not valid.")
		return ("You are done with this item")

	def showDescription(self):
		return self.description

	def showOptions(self):
		return self.options

	# 1 = look closer
	# 2 = interact
	# anything else = do nothing
	def interact(self, response, player):
		if response == "1":
			return (self.inspect)
		elif response == "2":
			return (self.interaction)
		elif response == "3":
			return (self.lootInventory(player))
		elif response == "4":
			return (self.placeIntoInventory(player))
		else:
			return ("You do nothing")

	# call method if you need to create the same object with a different inventory
	def createUnique(self, diffInventory):
		return WorldObject(diffInventory, self.ID, self.description, self.inspect, self.interaction)