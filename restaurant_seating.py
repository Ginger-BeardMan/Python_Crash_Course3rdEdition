dinner_party = input("How many guests will be attending the dinner party this evening?")

guest_count = int(dinner_party)

if guest_count > 8:
	print('Unfortunately, at this time there is a wait for that number of members. ')
	input('May I take your name? ')
else:
	print('We are able to seat you now. Please follow me. ')