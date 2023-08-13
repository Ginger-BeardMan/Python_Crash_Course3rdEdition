from pathlib import Path
import json


#prompt for user's favorite number
favorite_number = input('What is your favorite number? ')

#use json.dumps() to store this number in a file

contents = json.dumps(favorite_number)
path.write_text(contents)


#write a seperate program that reads in this value and prints the message 'I know our favorite number! It's ____.'

contents = path.read_text()
favorite_number = json.loads(contents)
print('I know your favorite number! It is {favorite_number}')