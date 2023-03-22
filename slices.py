# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

pizzas = ['Cheese', 'Pepperoni & Sausage', 'Hawaiian']

for pizza in pizzas:
	print(pizza)
	print(f"I like {pizza} pizza! It is yummy!")

print(f"My first favorite pizza is {pizzas[0]}, it is just simply delicious! My next favorite pizza is {pizzas[1]}, it has a little kick! My other favorite pizza is {pizzas[2]}, it has a tropical twist! I love pizzas!")

# Adding additional items to the pizza list for the slices.py script assignment

pizzas.append('Combo')
pizzas.append('Curry Chicken')
pizzas.append('Margarita')

# print the message The first three items in the list are: then use a slice to print the first three items from that program's list

print("The first three items in the list are:")
print(pizzas[:3])

# print the message The items in the middle of the list are: then use a slice to print the middle three items from that program's list

print("The items in the middle of the list are:")
print(pizzas[1:4])

# print the message The last three items in the list are: then use a slice to print the last three items from that program's list

print("The last three items in the list are:")
print(pizzas[-3:])