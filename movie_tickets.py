admission = "Please let me know the age of the ticket holder and I will let you know the price."
admission += "\nWhen everyone has a ticket, please state 'done'. "

total_cost = 0

while True:
	movie_ticket = input(admission)
	
	if movie_ticket == 'done':
		print(f'Your total cost for the movie today is ${total_cost}.')
		break
	else:
		age = int(movie_ticket)
		if age <= 3:
			print('That attendee will be free.')
		elif age <= 12:
			print('That attendee will cost $10')
			total_cost += 10
		elif age > 12:
			print('That attendee will cost $15')
			total_cost += 15