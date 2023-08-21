class Employee():

	def __init__(self, first_name, last_name, annual_salary):
		'''take in the name and salary of a worker'''
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = int(annual_salary)

	def give_raise(self):
		'''add 5k to salary by default, also allow a random input for a raise'''
		raise_total = input('How much of a raise will you get this year? 5k or different amount? ')
		if raise_total == '5k':
			self.annual_salary += 5000
			print(f'Your new salary is {self.annual_salary}')
		else:
			new_raise = input('What is the new total raise? ')
			self.annual_salary += int(new_raise)
			print(f'Your new salary is {self.annual_salary}')

employee_john = Employee('John', 'Smith', 100000)

print(f'Hello {employee_john.first_name} {employee_john.last_name}, your current salary is {employee_john.annual_salary}. Is a raise in order?')

employee_john.give_raise()