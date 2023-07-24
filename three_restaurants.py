class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f'{self.restaurant_name} creates a quiet atomosphere that is also welcoming and warm.')
		print(f'They serve the best {self.cuisine_type} in the city.')

	def open_restaurant(self):
		print(f'{self.restaurant_name} is now open!')

bbq_joint = Restaurant('Smokehaus', 'BBQ')

italian_joint = Restaurant('DeMaggios', 'Italian')

deli_joint = Restaurant('Mr. Pickles', 'Deli Sandwiches')

bbq_joint.describe_restaurant()
bbq_joint.open_restaurant()

italian_joint.describe_restaurant()
italian_joint.open_restaurant()

deli_joint.describe_restaurant()
deli_joint.open_restaurant()