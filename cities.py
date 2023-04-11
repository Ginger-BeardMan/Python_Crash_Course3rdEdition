cities = {
	'Manchester': {
	'country': 'United States',
	'population': 115644,
	'fact': 'largest city in New Hampshire'
	},
	'Concord': {
	'country': 'United States',
	'population': 43976,
	'fact': 'capital of New Hampshire'
	},
	'Conway': {
	'country': 'United States',
	'population': 9822,
	'fact': 'olympian Sean Doherty is from here'
	}
}

for city, information in cities.items():
	print(f"{city} is an interesting place, here is some information:")

	for fact_title, fact in information.items():
		print(f"{fact_title.title()} is {fact}")