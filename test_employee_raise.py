from employee import Employee

default_employee = Employee('John', 'Smith', 100000)

def test_give_default():
	'''assert that the default raise amount will work'''
	default_employee.give_raise()
	assert 'Your new salary is 105000'

def test_custom_raise():
	'''assert that a custom raise amount will work'''
	default_employee.give_raise('exceptional', 7705)
	assert 'Your new salary is 107705'