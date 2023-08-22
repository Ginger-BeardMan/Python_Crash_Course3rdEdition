#import pytest
from employee import Employee


#@pytest.fixture
def test_give_default():
	'''assert that the default raise amount will work'''
	default_employee = Employee('John', 'Smith', 100000)
	assert default_employee == 'Your new salary is 105000'

#def give_custom_raise():
#	'''assert that a custom raise amount will work'''
#	default_employee = Employee('John', 'Smith', 100000)
#	default_employee.give_raise('exceptional')
#	assert default_employee == 'Your new salary is 110000'