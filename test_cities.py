from city_country import get_city_country

def test_city_country():
	'''Does santiago, chile work?'''
	formatted_location = get_city_country('Santiago', 'Chile')
	assert formatted_location == 'Santiago, Chile'