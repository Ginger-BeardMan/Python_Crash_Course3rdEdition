class Users:

	def __init__(self, first_name, last_name, location, email, DOB):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.email = email
		self.DOB = DOB
		self.login_attempts = 0

	def describe_user(self):
		print(f'Welcome {self.first_name} {self.last_name}, below is the information we currently have on file:')
		print(f'{self.first_name} currently resides in {self.location}, prefers {self.email} for contact, and was born on {self.DOB}')

	def greet_user(self):
		print(f'We are always happy to see you {self.first_name} {self.last_name}, have a wonderful time!')

	def logging_in(self):
		print(f'You have attempted to login {self.login_attempts} times.')

	def update_logins(self, logins):
		self.loggin_in = logins

	def increment_login_attempts(self, logins):
		self.login_attempts += logins

	def reset_login_attempts(self):
		self.login_attempts = 0

user1 = Users('Sean', 'Connery', 'Scotland', '007@MI6.UK', '8.25.1930')
user1.logging_in()

user1.describe_user()
user1.greet_user()
user1.update_logins(1)
user1.logging_in()
user1.increment_login_attempts(1)
user1.logging_in()
user1.increment_login_attempts(1)
user1.logging_in()
user1.increment_login_attempts(1)
user1.logging_in()
user1.increment_login_attempts(1)
user1.logging_in()
user1.reset_login_attempts()
user1.logging_in()