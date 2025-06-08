from WorldObject import WorldObject

# governs simple doors (i.e. ones that don't need to be unlocked, can just open and close no issue)
class Door(WorldObject):
	def __init__(self, inventory, ID):
		self.ID = ID
		self.inventory = inventory
		self.description = ("You see a door.\n"
					  "It is chalk-white, with a grayish trim around the edges of the door.\n"
					  "The doorknob is to the center-right of the door itself, and is brass colored.\n"
					  "It is clean and has no dust or dirt on it.")
		self.inspect = ("The paint on the door appears to be a recent coat.\n"
						   "There is some noticable grain on the door, along with tiny bumps on the door.\n"
						   "The doorknob has fingerprint marks on it, from constant usage of staff and guests in the room.")
		self.options = ("-----\n"
					  "1. Look Closer\n"
					  "2. Interact\n"
					  "Any Other Option. Do Nothing")

	def alterDoor(self):
		self.ID *= -1

	def createUnique(self, diffInventory):
		return Door(diffInventory)

	# 1 = look closer
	# 2 = interact
	# anything else = do nothing
	def interact(self, response):
		if response == "1":
			return (self.inspect)
		elif response == "2":
			self.alterDoor()
			if self.ID > 0:
				return ("You grab the doorknob, and push the door away from you.\n"
							   "It locks into the door frame with a thud.\n"
							   "As you let go of the doorknob, it springs back into the locked position with a click.\n"
							   "It is now closed.")
			elif self.ID < 0:
				return ("You grab the doorknob, and twist it to the right.\n"
							   "The door unlocks as you pull it towards your body.\n"
							   "It is now open.")
		else:
			return ("You do nothing")

# governs simple locked doors
# isLocked is boolean
class LockedDoor(Door):
	def __init__(self, inventory, state, ID):
		self.ID = ID + 0.1
		self.inventory = inventory
		self.isLocked = state
		self.description = ("You see a door.\n"
					  "It is chalk-white, with a grayish trim around the edges of the door.\n"
					  "The doorknob is to the center-right of the door itself, and is brass colored.\n"
					  "It is clean and has no dust or dirt on it.\n"
					  "There is a rectangular hole below the knob.")
		self.inspect = ("The paint on the door appears to be a recent coat.\n"
						   "There is some noticable grain on the door, along with tiny bumps on the door.\n"
						   "The doorknob has fingerprint marks on it, from constant usage of staff and guests in the room.\n"
						   "There is also a brass plate on the door with a key shaped hole on it.")
		self.options = ("-----\n"
					  "1. Look Closer\n"
					  "2. Interact - doorknob\n"
					  "3. Interact - lock\n"
					  "Any Other Option. Do Nothing")

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

	def interact(self, response):
		if response == "1":
			return (self.inspect)
		elif response == "2":
			if self.isLocked:
				return ("This door is locked.")
			else:
				self.alterDoor()
				if self.ID > 0:
					return ("You grab the doorknob, and push the door away from you.\n"
								   "It locks into the door frame with a thud.\n"
								   "As you let go of the doorknob, it springs back into the locked position with a click.\n"
								   "It is now closed.")
				elif self.ID < 0:
					return ("You grab the doorknob, and twist it to the right.\n"
								   "The door unlocks as you pull it towards your body.\n"
								   "It is now open.")
		elif response == "3":
			if self.isLocked:
				self.unlockDoor()
				return ("You unlock the door. The door is now unlocked.")
			else:
				self.lockDoor()
				return ("You lock the door. The door is now locked.")
		else:
			return ("You do nothing.")

# governs doors that are locked via code (touchpad or multi dial based locks)
# isLocked is boolean
class CodeLockedDoor(LockedDoor):
	def __init__(self, inventory, state, code, ID):
		self.ID = ID + 0.2
		self.inventory = inventory
		self.isLocked = state
		self.code = code
		self.description = ("You see a door.\n"
					  "It is chalk-white, with a grayish trim around the edges of the door.\n"
					  "The doorknob is to the center-right of the door itself, and is brass colored.\n"
					  "It is clean and has no dust or dirt on it.\n"
					  "There is a phone style keypad below the doorknob.")

	def unlockDoor(inputtedCode):
		if inputtedCode == self.code:
			self.isLocked = False

	def createUnique(self, diffInventory, diffState, code):
		return LockedDoor(diffInventory, diffState, code)
