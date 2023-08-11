#taking input for the first number
first_num = input("First equation number: ")

#taking input for the second number
second_num = input("Second equation number: ")

#try/except if the input is not an int
try:
	print(int(first_num) + int(second_num))
except ValueError:
	print("That's not a number!")