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

user1 = Users('Sean', 'Connery', 'Scotland', '007@MI6.UK', '8.25.1930')

user2 = Users('Keanu', 'Reeves', 'Lebanon', 'ted@billandted.com', '9.2.1964')

user3 = Users('George', 'Carlin', 'NYC', 'team@yournotonit.com', '5.12.1937')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()