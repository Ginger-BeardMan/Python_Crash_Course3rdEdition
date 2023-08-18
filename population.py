def get_city_country(city, country, population=''):
	if population:
		city_country = f'{city}, {country}, Population: {population}'
	else:
		city_country = f'{city}, {country}'
	'''return a single string of the form city, country'''
	return city_country.title()