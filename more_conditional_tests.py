computer = 'Linux'

if computer == 'Linux':
	print(computer == 'Linux')
	print('Great choice!')
else:
	print(computer != 'Linux')
	print('What are you thinking?!?')


favorite_cars = ['lamborghini', 'ferrari', 'koenigsegg']

if 'lamborghini' in favorite_cars:
	print('I like your style!')

if 'Chevy' in favorite_cars:
	print('Chevy' in favorite_cars)
	print('Me no likey')
else:
	print('Chevy' in favorite_cars)
	print("I'm glad you don't like Chevys!")


child_1 = 5
child_2 = 3

if child_1 < 21 and child_2 < 21:
	print('No drinking for those children!!')

if child_1 > 4 or child_2 > 4:
	print('Nice, you had some kids.')

user_name = 'JoeMaMAisSeXY'

if user_name.lower() == 'joemamaissexy':
	print('User is banned, go back to the 90s...')

my_age = 33

print(my_age == 10)
print(my_age < 50)
print(my_age <= 35)
print(my_age > 35)
print(my_age >= 21)