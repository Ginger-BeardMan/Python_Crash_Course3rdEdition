class Users:

	def __init__(self, first_name, last_name, location, email, DOB):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.email = email
		self.DOB = DOB

	def describe_user(self):
		print(f'Welcome {self.first_name} {self.last_name}, below is the information we currently have on file:')
		print(f'{self.first_name} currently resides in {self.location}, prefers {self.email} for contact, and was born on {self.DOB}')

	def greet_user(self):
		print(f'We are always happy to see you {self.first_name} {self.last_name}, have a wonderful time!')

class Admin(Users):

	def __init__(self, first_name, last_name, location, email, DOB):
		super().__init__(first_name, last_name, location, email, DOB)
		self.privileges = Privileges()

class Privileges:

	def __init__(self):
		self.privileges = ['can add a post', 'can delete post', 'can ban users']

	def show_privileges(self):
		print(f'The administrator {self.privileges[0]}, {self.privileges[1]}, and {self.privileges[2]}.')

admin_user = Admin('John', 'Smith', 'Silicon Valley', 'watchingyou@meta.org', 'July 4, 1776')

admin_user.describe_user()
admin_user.greet_user()
admin_user.privileges.show_privileges()