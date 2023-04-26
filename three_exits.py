order = "I am here to take your order, please let me know what toppings you would like on your pizza: "

toppings = []

while True:
	topping = input(order)
	
	if topping != 'done' and topping != 'finished':
		toppings.append(topping)

	if len(toppings) == 5:
		print("You've reached the maximum amount of toppings for one pizza.")
		print(f"I will finish your pizza with {toppings[0]}, {toppings[1]}, {toppings[2]}, {toppings[3]}, & {toppings[4]} in just a momment!")
		break
	else:
		print(f"Your toppings are now: {toppings}.")