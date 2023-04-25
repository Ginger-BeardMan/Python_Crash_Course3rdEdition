
order = "I am here to take your order, please let me know what toppings you would like on your pizza"
order += "\nWhen you are done, please enter 'done' or 'finished'. "

toppings = []

while True:
	topping = input(order)
	
	if topping != 'done' and topping != 'finished':
		toppings.append(topping)

	if topping == 'done' or topping == 'finished':
		print(f"I will finish your pizza with {toppings} in just a momment!")
		break
	else:
		print(f"Your toppings are now: {toppings}.")