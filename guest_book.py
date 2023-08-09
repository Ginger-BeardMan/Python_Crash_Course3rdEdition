from pathlib import Path

path = Path('guest.txt')

guest_list = []

guests = ''

while True:
	guest_name = input("Please enter your first and last name: ")
	guest_list.append(guest_name)
	response = input("Do you want to continue: ")
	if response == 'yes':
		True
	else:
		print(guest_list)
		for name in guest_list:
			guests += (name.title() + '\n')
		path.write_text(guests)
		break