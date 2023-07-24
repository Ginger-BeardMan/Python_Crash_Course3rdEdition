class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'{self.restaurant_name} creates a quiet atomosphere that is also welcoming and warm.')
		print(f'They serve the best {self.cuisine_type} in the city.')

	def open_restaurant(self):
		print(f'{self.restaurant_name} is now open!')

local_restaurant = Restaurant("Willie's", 'BBQ')

local_restaurant.describe_restaurant()
local_restaurant.open_restaurant()