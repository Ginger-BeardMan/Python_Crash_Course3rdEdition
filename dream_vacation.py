favorite_locations = {}

open_poll = True

while open_poll:
	traveler = input('What is your name? ')
	
	travel_information = input('If you could travel to anywhere in the world where would you go? ')

	favorite_locations[traveler] = travel_information

	repeat = input('Would you like to let the next user answer the poll? ')

	if repeat == 'no':
		open_poll = False

print('----Poll Results----')

for traveler, travel_information in favorite_locations.items():
	print(f"{traveler.title()} dreams of traveling to {travel_information.title()}, that sounds like a wonderful place!")