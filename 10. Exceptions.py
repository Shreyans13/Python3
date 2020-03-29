try:
	print(5/0)
except ZeroDivisionError:
	print("You can`t divide by zero!!!!")

print ("Give me two numbers, and i`ll divide them")

# # The else block and Try and Except 
# while True:
# 	first_number = input("\nFirst Number: ")
# 	if first_number == 'q':
# 		break
# 	second_number = input("Secon Number: ")
# 	if second_number == 'q':
# 		break
# 	try:
# 		answer = int(first_number)//int(second_number)
# 	except ZeroDivisionError:
# 		print("You can`t divide by zero!!!!")
# 	else:
# 		print(answer)

# Handling the FileNotFoundError Exception
def count_words(filename):
	try:
		with open(filename, encoding = 'utf-8') as f:
			contents = f.read()
	except:
		# print(f"File:{filename} does not exist.")
		# Failing silently
		pass
	else:
		# Count the approximate numbers of word in the file
		words = contents.split()
		num_words = len(words)
		print(f"The file {filenamee} has about {num_words} words.")

filenames = ['i.txt', 'am.txt', 'a.txt', 'good.txt', 'programmer.txt']
for filename in filenames:
	count_words(filename)