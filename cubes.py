# Make a list of the first 10 cubes(the cube of integers 1 to 10), and use a for loop to print out the value of each cube.

cubes = [value**3 for value in range(1, 11)]

for cube in cubes:
	print(cube)