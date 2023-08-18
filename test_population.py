from population import get_city_country

def test_population():
	formatted_location = get_city_country('Santiago', 'Chile')
	assert formatted_location == 'Santiago, Chile'

def test_city_country_population():
	formatted_location = get_city_country('Santiago', 'Chile', '5000000')
	assert formatted_location == 'Santiago, Chile, Population: 5000000'