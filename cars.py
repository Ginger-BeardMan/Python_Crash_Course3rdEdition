def car_info(manufacturer, model, **car_make):
	car_make['manufacturer'] = manufacturer
	car_make['model'] = model
	return car_make

car_profile = car_info('Toyota', 'Tacoma', color = 'Orange', tow_package = True)

print(f'car = {car_profile}') 