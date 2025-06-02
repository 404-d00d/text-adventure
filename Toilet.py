from WorldObject import WorldObject

class Toilet(WorldObject):
	def __init__(self, inventory):
		self.ID = 3.1
		self.inventory = inventory

	def flushToilet(self):
		self.ID = 3