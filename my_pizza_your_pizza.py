# Start with your program from Exercise 4.1. Make a copy of the list of pizzas, and call it friend_pizzas.
my_pizzas = ['Cheese', 'Pepperoni & Sausage', 'Hawaiian']
friend_pizzas = my_pizzas[:]

for pizza in my_pizzas:
	print(pizza)
	print(f"I like {pizza} pizza! It is yummy!")

print(f"My first favorite pizza is {my_pizzas[0]}, it is just simply delicious! My next favorite pizza is {my_pizzas[1]}, it has a little kick! My other favorite pizza is {my_pizzas[2]}, it has a tropical twist! I love pizzas!")

# Add a new pizza to the original list

my_pizzas.append('Curry Chicken')

# Add a different pizza to the list friend_pizza

friend_pizzas.append('Combo')

# prove that you have two seperate lists. 

print("My favorite pizzas are:")
for pizza in my_pizzas:
	print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)