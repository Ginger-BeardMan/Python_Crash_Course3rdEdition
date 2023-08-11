print('Enter q to quit at any time.')

#loop through the calculator until the user stops the program
while True:

	#taking input for the first number
	first_num = input("First equation number: ")
	if first_num == 'q':
		break

	#taking input for the second number
	second_num = input("Second equation number: ")
	if second_num == 'q':
		break

	#try/except if the input is not an int
	try:
		answer = int(first_num) + int(second_num)
		print(answer)
		continue
	except ValueError:
		print("That's not a number!")
		continue