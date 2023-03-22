# A buffet style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

simple_foods = ('chicken', 'beef', 'brocolli', 'carrot', 'potato')
print(simple_foods)

# Use a for loop to print each food the restaurant offers

for food in simple_foods:
	print(food)

# Try to modify one of the items, and make sure that Python rejects the change

simple_foods[0] = 'fish'

# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

simple_foods = ('chicken', 'beef', 'corn', 'peas', 'potato')
print(simple_foods)

for food in simple_foods:
	print(food)