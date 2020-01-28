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

def message(user = 'user'): #default value
# Multiple default values can also be set.
    print (f"\tHello, {user.title()}") #Display a greeting a message

message("Shreyans Jain")
message()
#optional argument value
def get_formatted_name(first_name, last_name,  middle_name=''):
    message = f"\tWe are hackers, and hackers have black terminals with green font.\n"
    if middle_name:
        return f"{message.upper()} \t\t{first_name} {middle_name} {last_name}"
    return f"{message.upper()} \t\t{first_name} {middle_name} {last_name}"

print(get_formatted_name('Shreyans','Jain'))
print(get_formatted_name('Suraj', 'Kumar', 'Singh'))


print (f"\tDictionary Builder")
def build_dictionary(first_name, last_name, age = None):
    person = {
    'name' : f"{first_name} {last_name}"
    }
    if age:
        person['age'] = age
    return person
print ("\tDictionary : ",build_dictionary("Shreyans", "Jain",age = 20))
print ("\tDictionary : ",build_dictionary(input("\tEnter your first name : "), input("\tEnter your last name : ")))
