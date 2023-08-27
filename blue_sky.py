import sys
import pygame

from bs_ship import BSShip

class BlueSky:

	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.bg_color = (230, 230, 230)
		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption('Blue Sky')
		self.ship = BSShip(self)
	
	def show_screen(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			self.screen.fill(self.bg_color)
			self.ship.show_ship()
			self.clock.tick(60)
			pygame.display.flip()

if __name__ == '__main__':
	bs = BlueSky()
	bs.show_screen()