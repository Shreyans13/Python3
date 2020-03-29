'''
The JSON (JavaScript Object Notation) format was originally developed for JavaScript.
However, it has since become a common format used by many languages, including
Python.
'''
# Number Writer
import json

numbers = [1, 3, 5, 11, 13, 17]

filename = 'numbers.json'

with open(filename, 'w') as f:
	json.dump(numbers, f)

# Numer Reader
# import json
filename = 'numbers.json'

with open(filename) as f:
	numbers = json.load(f)

print(numbers)
