from random import choices

#all paramiters have been defined:

character_choices = [66]#, 93, 42, 5, 18, 99, 31, 2, 7, 26, 'A', 'G', 'S', 'K', 'Z']

my_ticket = [66, 66, 66, 66]

count = 0

winning_numbers = []

def get_ticket_num():
	winning_numbers = []
	while len(winning_numbers) < 4:
		winning_numbers += (choices(character_choices))
		print(winning_numbers)

def check_winning_ticket():
	if my_ticket == winning_numbers:
		print('Congratulations, you won one billion dollars!')
		count+=1
		print(count)

while winning_numbers != my_ticket:
	get_ticket_num()
	check_winning_ticket()