def sandwich(*ingredients):
	print('I will get started making that sandwich with the following:')
	for ingredient in ingredients:
		print(f'- {ingredient}')

sandwich('ham', 'mustard', 'swiss cheese', 'tomato')
sandwich('turkey', 'jalapenos', 'pepper jack cheese', 'tomato', 'lettuce', 'onion')