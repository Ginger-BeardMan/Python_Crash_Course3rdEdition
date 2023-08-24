from employee import Employee

def test_custom_raise():
	'''assert that a custom raise amount will work'''
	default_employee = Employee('John', 'Smith', 100000)
	default_employee.give_raise('exceptional', 7705)
	assert 'Your new salary is 107705'