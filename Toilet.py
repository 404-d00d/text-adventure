from WorldObject import WorldObject

class Toilet(WorldObject):
	def __init__(self, inventory, ID):
		self.ID = ID
		self.inventory = inventory
		self.description = ("You see a toilet.\n"
					  "It is porcelain white, with no blemishes or marks on the body.\n"
					  "The tank lid and tank of the toilet appear to be bolted to the toilet basin and the wall itself.\n"
					  "The toilet lid and toilet basin are white and clean as the rest of the toilet.\n"
					  "The toilet is shiny, reflecting the light from the celing light tubes.\n"
					  "The toilet lid is closed.")
		self.inspect = ("You lift up the toilet lid.\n"
							  "The bowl is filled with water, chunks of food, and bile.\n"
							  "The bile and food chunks float on the water's surface, and are mixed together cleanly.\n"
							  "It's hard to tell what is bile and what are the food chunks.\n"
							  "You immediately close the toilet lid, just to avoid adding more to that accursed pile.")

		self.interaction = ("You push down on the toilet handle on the tank.\n"
						  "You hear the sound of water flowing into the toilet bowl, followed by the sound of water rushing down the pipes.\n"
						  "It's eventually followed by the rush of water back into the toilet basin.")
		self.options = ("-----\n"
					  "1. Look Closer\n"
					  "2. Interact\n"
					  "3. Show Inventory\n"
					  "Any Other Option. Do Nothing")

	def flushToilet(self):
		self.inspect = ("You lift up the toilet lid.\n"
							  "The bowl is clear and clean.\n"
							  "The water in the bowl is transparent, letting you see the inside of the toilet bowl.\n"
							  "Much like the outside of the toilet, the inside of the basin is white.")

	def interact(self, response, player):
		if response == "1":
			return (self.inspect)
		elif response == "2":
			self.flushToilet()
			return (self.interaction)
		elif response == "3":
			return (self.lootInventory(player))
		else:
			return ("You do nothing")

	def createUnique(self, diffInventory):
		return WorldObject(diffInventory, self.ID, self.description, self.inspect, self.interaction)

