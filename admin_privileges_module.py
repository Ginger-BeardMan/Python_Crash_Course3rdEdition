from users_module import Users

class Admin(Users):

	def __init__(self, first_name, last_name, location, email, DOB):
		super().__init__(first_name, last_name, location, email, DOB)
		self.privileges = Privileges()

class Privileges:

	def __init__(self):
		self.privileges = ['can add a post', 'can delete post', 'can ban users']

	def show_privileges(self):
		actions = f'The administrator {self.privileges[0]}, {self.privileges[1]}, and {self.privileges[2]}.'
		return actions