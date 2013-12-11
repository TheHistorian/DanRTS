import pygame, os

class Image:
	def __init__(self, filename):
		self.filename = filename
		self.load()
		self.location = 0, 0
		self.bounds = self.image.get_rect()
		self.dirty = True
			
	def load(self, filename = None):
		if filename == None:
			filename = self.filename
		self.image = pygame.image.load(os.path.join("Images", filename))
		if(filename[-3:] == "png"
		or filename[-3:] == "gif"):
			self.image = self.image.convert_alpha()		

	def move(self, x, y):
		self.location = x, y
		
	def move_rel(self, x, y):
		self.move(self.location[0] + x, self.location[1] + y)
	
