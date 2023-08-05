from random import randint

class Die:

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		roll = randint(1, self.sides)
		return roll

my_die = Die()
ten_die = Die(10)
twenty_die = Die(20)

print('This is my standard die!')
print(my_die.roll_die())
print(my_die.roll_die())
print(my_die.roll_die())
print(my_die.roll_die())
print(my_die.roll_die())
print(my_die.roll_die())
print(my_die.roll_die())
print(my_die.roll_die())
print(my_die.roll_die())
print(my_die.roll_die())

print('This is my 10 sided die!')

print(ten_die.roll_die())
print(ten_die.roll_die())
print(ten_die.roll_die())
print(ten_die.roll_die())
print(ten_die.roll_die())
print(ten_die.roll_die())
print(ten_die.roll_die())
print(ten_die.roll_die())
print(ten_die.roll_die())
print(ten_die.roll_die())

print('This is my 20 sided die!')

print(twenty_die.roll_die())
print(twenty_die.roll_die())
print(twenty_die.roll_die())
print(twenty_die.roll_die())
print(twenty_die.roll_die())
print(twenty_die.roll_die())
print(twenty_die.roll_die())
print(twenty_die.roll_die())
print(twenty_die.roll_die())
print(twenty_die.roll_die())