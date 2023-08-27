import pygame

class BSShip:
	def __init__(self, bs_game):
		#initialize the ship and set it's starting position
		self.screen = bs_game.screen
		self.screen_rect = bs_game.screen.get_rect()

		#load the ship image and get it's rectangle
		self.image = pygame.image.load('shiper_mix_02.bmp')
		self.rect = self.image.get_rect()

		#start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

	def show_ship(self):
		#draw the ship at it's current location
		self.screen.blit(self.image, self.rect)