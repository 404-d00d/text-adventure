class Map:
	# id is map Id, cells is 2d array of all world objects making the map, mapDict is a dict with value as dict
	def __init__(self, ID, cells, mapDict, mapSummary):
		self.ID = ID
		self.cells = cells
		self.connectingRooms = mapDict
		self.mapSummary = mapSummary

	def getMap(self):
		return self.cells

	def getID(self):
		return self.ID

	def getConnections(self):
		return self.connectingRooms

	def getSpecificCell(self, X, Y):
		return self.cells[Y][X]

	def getMapSummary(self):
		return self.mapSummary
