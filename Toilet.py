from WorldObject import WorldObject

class Toilet(WorldObject):
	def __init__(self, inventory):
		self.ID = 3.1
		self.inventory = inventory
		self.description = ("You see a toilet.\n"
					  "It is porcelain white, with no blemishes or marks on the body.\n"
					  "The tank lid and tank of the toilet appear to be bolted to the toilet basin and the wall itself.\n"
					  "The toilet lid and toilet basin are white and clean as the rest of the toilet.\n"
					  "The toilet is shiny, reflecting the light from the celing light tubes.\n"
					  "The toilet lid is closed.")

	def flushToilet(self):
		self.ID = 3