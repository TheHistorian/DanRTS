import pygame, sys

class Window:
	def __init__(self, title, height):
		self.title = title
		self.height = height
		self.width = int(height * (16.0 / 9.0)) # 16:9 aspect ratio
		self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
		pygame.display.set_caption(title)
		self.background = pygame.rect.Rect(0, 0, self.width, self.height)
		self.images = []
		
	def add(self, image):
		self.images.append(image)
		image.dirty = True				

	def draw(self):
		pygame.draw.rect(self.screen, (0, 0, 0), self.background)
		for image in self.images:
			if image.dirty:
				self.screen.blit(image.image, image.location)
		pygame.display.update()

	def events(self):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT 
			or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
				pygame.quit()
				sys.exit()
		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.images[0].move_rel(0, -5)
		if keys[pygame.K_s]:
			self.images[0].move_rel(0, 5)
		if keys[pygame.K_a]:
			self.images[0].move_rel(-5, 0)
		if keys[pygame.K_d]:
			self.images[0].move_rel(5, 0)
	
