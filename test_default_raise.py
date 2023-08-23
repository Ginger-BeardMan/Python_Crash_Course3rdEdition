import pytest
from employee import Employee

def test_give_default():
	'''assert that the default raise amount will work'''
	default_employee = Employee('John', 'Smith', 100000)
	assert default_employee.give_raise() == 'Your new salary is 105000'