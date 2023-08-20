class Employee():

	attributes = []

	def __init__(self, first_name, last_name, annual_salary):
		'''take in the name and salary of a worker'''
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = int(annual_salary)

	def give_raise(self):
		'''add 5k to salary by default, also allow a random input for a raise'''
		raise_total = input('How much of a raise will you get this year? 5k or different amount? ')
		if raise_total == '5k':
			annual_salary += 5000
			return annual_salary
		else:
			new_raise = input(int('What is the new total raise? '))
			annual_salary += new_raise
			return annual_salary


