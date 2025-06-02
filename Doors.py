from WorldObject import WorldObject

# governs simple doors (i.e. ones that don't need to be unlocked, can just open and close no issue)
class Door(WorldObject):
	def __init__(self, inventory):
		self.ID = 2
		self.inventory = inventory

	def alterDoor(self):
		self.ID *= -1

	def createUnique(self, diffInventory):
		return Door(diffInventory)

# governs simple doors (i.e. ones that don't need to be unlocked, can just open and close no issue)
# isLocked is boolean
class LockedDoor(Door):
	def __init__(self, inventory, state):
		self.ID = 2.1
		self.inventory = inventory
		self.isLocked = state

	def alterDoor(self):
		if not self.isLocked:
			self.ID *= -1

	def unlockDoor(self):
		self.isLocked = False

	def lockDoor(self):
		self.isLocked = True

	def getLockState(self):
		return self.isLocked

	def createUnique(self, diffInventory, diffState):
		return LockedDoor(diffInventory, diffState)

# governs doors that are locked via code (touchpad or multi dial based locks)
# isLocked is boolean
class CodeLockedDoor(LockedDoor):
	def __init__(self, inventory, state, code):
		self.ID = 2.2
		self.inventory = inventory
		self.isLocked = state
		self.code = code

	def unlockDoor(inputtedCode):
		if inputtedCode == self.code:
			self.isLocked = False

	def createUnique(self, diffInventory, diffState, code):
		return LockedDoor(diffInventory, diffState, code)