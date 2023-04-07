favorite_places = {
	'Ron': ['Kenya', 'China'],
	'Dandy': ['Thailand', 'Iceland', 'Egypt'],
	'Misti': ['Chile'],
}

for person, places in favorite_places.items():
	if len(places) > 1:
		print(f"{person.title()}'s favorite places are:")
		for place in places:
			print(f"\t{place.title()}")
	else:
		print(f"{person.title()}'s favorite place is:")
		for place in places:
			print(f"\t{place.title()}")