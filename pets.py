first_pet = {'name': 'Rowly','owner': 'Rod'}
second_pet = {'name': 'Spiner','owner': 'Sally'}
third_pet = {'name': 'Flik','owner': 'Frank'}
fourth_pet = {'name': 'Lucky','owner': 'Lucy'}

pets = [first_pet, second_pet, third_pet, fourth_pet]


for pet in pets:
	for key, value in pet.items():
		print(f"{key}: {value}")