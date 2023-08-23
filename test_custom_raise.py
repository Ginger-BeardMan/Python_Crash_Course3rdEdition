import pytest
from employee import Employee

def give_custom_raise():
	'''assert that a custom raise amount will work'''
	default_employee = Employee('John', 'Smith', 100000)
	default_employee.give_raise('exceptional', 7705)
	assert default_employee == 'Your new salary is 107705'