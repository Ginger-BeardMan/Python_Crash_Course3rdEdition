from random import randint
class Employee:

	def __init__(self, first_name, last_name, annual_salary,):
		'''take in the name and salary of a worker'''
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = int(annual_salary)
		

	def give_raise(self, exceptionality='', salary_raise=''):
		'''add 5k to salary by default, allow for a random raise the the employee is exceptional'''
		self.exceptionality = exceptionality
		self.salary_raise = salary_raise
		if exceptionality and salary_raise:
			self.annual_salary += int(self.salary_raise)
			print(f'Your new salary is {self.annual_salary}')
		else:
			self.annual_salary += 5000
			print(f'Your new salary is {self.annual_salary}')

#employee_john = Employee('John', 'Smith', 100000)

#employee_john.give_raise('exceptional', 7705)