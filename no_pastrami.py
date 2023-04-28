sandwich_orders = ['cuban', 'pastrami', 'monte cristo', 'club sandwich', 'pastrami', 'breakfast sandwich', 'roast beef', 'panini', 'pastrami']

finished_sandwiches = []

print(f'Ordered sandwiches: {sandwich_orders}')

print('The deli has run out of pastrami for the day.')

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	completed_sandwich = sandwich_orders.pop()

	finished_sandwiches.append(completed_sandwich)

	print(f'I have made your {completed_sandwich.title()}')

print(f"Completed sandwiches: {finished_sandwiches}")