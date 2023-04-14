car_type = input('What type of vehicle would you like to rent today?: ')

brand = input("What brand of car is preferred?(if none, indicate 'no preference'): ")

if brand != 'no preference':
	model = input("Lastly, what model from that brand is preferred? (if none, indicate 'no preference'): ")

print('Great, thank you for that information')

if brand != 'no preference' and model != 'no preference':
	print(f'Let me take a look to see if we have a {car_type} that is a {brand.title()} {model.title()}')
elif brand != 'no preference' and model == 'no preference':
	print(f'Let me take a look to see if we have a {brand.title()} {car_type}')
elif brand == 'no preference':
	print(f'Let me check if we have any vehicle that is a {car_type}')