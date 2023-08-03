class Users:

	def __init__(self, first_name, last_name, location, email, DOB):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.email = email
		self.DOB = DOB

	def describe_user(self):
		user_info = f'Welcome {self.first_name} {self.last_name}, below is the information we currently have on file: {self.first_name} currently resides in {self.location}, prefers {self.email} for contact, and was born on {self.DOB}'
		return user_info

	def greet_user(self):
		greeting = f'We are always happy to see you {self.first_name} {self.last_name}, have a wonderful time!'
		return greeting