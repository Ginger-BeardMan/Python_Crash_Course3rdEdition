# Choose a version of foods.py and write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('canoli')
friends_foods.append('ice cream')

for food in my_foods:
	print(food)

for food in friends_foods:
	print(food)