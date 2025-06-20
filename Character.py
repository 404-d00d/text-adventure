class Character:
	# id, x, y, direction, and room are ints
	# 1 = N, 2 = E, 3 = S, 4 = W
	def __init__(self, iD, x, y, direction, room, inventory):
		self.id = iD
		self.x = x
		self.y = y
		self.direction = direction
		self.room = room
		self.inventory = inventory

	def getID(self):
		return self.id

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getDirection(self):
		return self.direction

	def getRoom(self):
		return self.room

	def changeRoom(self, newRoomID):
		self.room = newRoomID

	def getInventory(self):
		return self.inventory

	def showInventory(self):
		print("===")
		print("PLAYER INVENTORY")
		for x in range(len(self.inventory)):
			print(str(x)+": "+str(self.inventory[x].getQuantity())+" "+self.inventory[x].getName())

	def removeItem(self, item):
		self.inventory.remove(item)

	def addItem(self, item):
		self.inventory.append(item)

	# only for setting the character positions when they move to the next room
	def setX(self, newX):
		self.x = newX

	def setY(self, newY):
		self.y = newY

	# handles direction regarding character interaction
	def charDirection(self, direction):
		x1, y1 = {
			1: (0, -1),  # N
			2: (1, 0),   # E
			3: (0, 1),   # S
			4: (-1, 0),  # W
		}[direction]
		return x1, y1

	# moves character (either via rotation or movement)
	def moveCharacter(self, mapCord, command):
		# Step 1: Rotate character
		if command == "right":  # turn right
			self.direction = (self.direction % 4) + 1
			return
		elif command == "left":  # turn left
			self.direction = 4 if self.direction == 1 else self.direction - 1
			return

		# Step 2: Determine movement vector based on command and direction
		forwardMap = {
			'forward': 0,
			'sideleft': 3,
			'backward': 2,
			'sideright': 1
		}
		if command not in forwardMap:
			return  # invalid movement key

		# Rotate direction to get movement vector
		direction = self.direction
		offset = (forwardMap[command] + direction - 1) % 4 + 1

		dx, dy = self.charDirection(offset)

		# Step 3: Calculate new position
		newX = self.x + dx
		newY = self.y + dy

		# Step 4: Check boundaries
		if 0 <= newY < len(mapCord) and 0 <= newX < len(mapCord[0]):
			# Step 5: Check for passable tile
			if mapCord[newY][newX].getID() <= 0:
				self.x = newX
				self.y = newY
