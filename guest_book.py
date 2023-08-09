from pathlib import Path

path = Path('guest.txt')

guest_list = []

while True:
	guest_name = input("Please enter your first and last name: ")
	guest_list.append(guest_name)
	response = input("Do you want to continue: ")
	if response == 'yes':
		True
	else:
		for name in guest_list:
			path.write_text(name + '\n')
		break