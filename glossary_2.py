# clean up code from glossary.py using loops

key_words = {'string': 'arrays of bytes representing unicode characters', 
	'variable': 'containers for storing data values', 
	'class': 'an object constructor', 
	'integer': 'a whole number without decimals of unlimited length', 
	'loop': 'used for iterating over a sequence'
	}

key_words['key'] = 'an item in a dictionary'
key_words['value'] = 'the definition of or object of a key in a dictionary'
key_words['function'] = 'a block of code which only runs when it is called'
key_words['if statement'] = 'a condition to be met in order for the block of code proceding the statement to run'
key_words['else'] = 'code that runs if all other conditions within an if statement are not met'

# print(f"string: {key_words['string']}\nvariable: {key_words['variable']}\nclass: {key_words['class']}\ninteger: {key_words['integer']}\nloop: {key_words['loop']}")

for word, definition in key_words.items():
	print(word.title() + ":")
	print(definition)