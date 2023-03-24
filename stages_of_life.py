# Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then write the script.

person_age = 33

if person_age < 2:
	print("You are a baby!")
elif person_age < 4:
	print("You are a toddler now!")
elif person_age < 13:
	print("Uh oh, pre teen years!")
elif person_age < 20:
	print("Can this teen move out already?!?")
elif person_age < 65:
	print('Why did my adult child move out!?! I miss them...')
elif person_age >= 65:
	print('How am I still alive with an elderly child?')