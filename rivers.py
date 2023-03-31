# make a dictionary containing three major rivers and the country each river runs through.

rivers = {'nile': 'egypt',
	'mississippi': 'the united states',
	'vistula': 'poland'}

for river, country in rivers.items():
	print(f"The {river.title()} flows through the country of {country.title()}")
	print(river.title())
	print(country.title())