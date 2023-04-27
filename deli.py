sandwich_orders = ['cuban', 'monte cristo', 'club sandwich', 'breakfast sandwich', 'roast beef', 'panini']

finished_sandwiches = []

while sandwich_orders:
	completed_sandwich = sandwich_orders.pop()

	finished_sandwiches.append(completed_sandwich)

	print(f'I have made your {completed_sandwich.title()}')