from employee import Employee

def test_give_default():
	'''assert that the default raise amount will work'''
	default_employee = Employee('John', 'Smith', 100000)
	default_employee.give_raise()
	assert 'Your new salary is 105000'