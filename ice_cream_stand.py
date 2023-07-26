class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'{self.restaurant_name} creates a quiet atomosphere that is also welcoming and warm.')
		print(f'They serve the best {self.cuisine_type} in the city.')

	def open_restaurant(self):
		print(f'{self.restaurant_name} is now open!')

class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', 'strawberry']

	def get_flavors(self):
		print(f'They currently serve {self.flavors[0], self.flavors[1], self.flavors[2]}')


best_stand = IceCreamStand('King Kone', 'Ice Cream')

best_stand.describe_restaurant()
best_stand.open_restaurant()
best_stand.get_flavors()