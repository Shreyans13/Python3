print("Functions")
def greet_user(user):
    print (f"\tHello, {user.title()}") #Display a greeting a message

# greet_user()
greet_user(input("\tEnter your name : ")) # Passing Function

# Positional Arguments
print()
def describe_pet(animal_type, pet_name): # order matters in Positional Arguments
    print (f"\n\tI have a {animal_type}")
    print (f"\tMy {animal_type}'s name is {pet_name.title()}")

describe_pet('Dog','leo') #animal_type = Dog and  pet_name = leo
describe_pet('Dog','bhirav') #Multiple Function calls
describe_pet(animal_type = 'Cat', pet_name = 'kitty') #keyword Arguments
# or
describe_pet(pet_name = 'rosie', animal_type = 'Cat')

def message(user = 'user'):
    print (f"\tHello, {user.title()}") #Display a greeting a message

message("Shreyans Jain")
message()
