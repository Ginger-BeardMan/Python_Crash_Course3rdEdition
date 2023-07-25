class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f'{self.restaurant_name} creates a quiet atomosphere that is also welcoming and warm.')
		print(f'They serve the best {self.cuisine_type} in the city.')

	def open_restaurant(self):
		print(f'{self.restaurant_name} is now open!')

	def display_served(self):
		print(f'We have successfully served {self.number_served} customers today!')

	def update_customers(self, served):
		self.number_served = served

	def increment_number_served(self, served):
		self.number_served += served

restaurant = Restaurant("Willie's", 'BBQ')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.update_customers(500)
restaurant.display_served()
restaurant.increment_number_served(50)
restaurant.display_served()