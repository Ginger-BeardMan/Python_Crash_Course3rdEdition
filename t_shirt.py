def make_shirt(size, shirt_text):
	print(f'You have ordered a shirt sized {size} with the message "{shirt_text.title()}" on it.')
	print('Please allow 3-5 business days to create.')

make_shirt('small', "ride the lightning")

make_shirt(size = 'medium', shirt_text = "I wanna rock and roll all night")