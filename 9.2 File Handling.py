filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.");

"""
You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
you to read and write to the file ('r+'). If you omit the mode argument,
Python opens the file in read-only mode by default
"""

# Writing  Multiple lines

filename = 'programming.txt'

with open(filename,'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love writing scripts.\n")

with open(filename,'a') as file_object:
	file_object.write("I love creating apps that can run in browser.\n")
	file_object.write("I love creaing pages using Djanjo.\n")
