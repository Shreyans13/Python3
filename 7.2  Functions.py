# Passing a list
import random
print ("Passing a list")
def users(names):
    confirmed_names = names[random.randint(0,4)]
    print("\t",confirmed_names)

usernames = [
    'Shreyans Jain',
    'Gurpreet Singh',
    'Priyanka Mukherjee',
    'S Puja',
    'Utkarsh'
    ]
users(usernames)

print ("\nModifying a list in the function")

# Modifying the list in the function is permanent
admin=[]
print (f"\tBefore function call admin = {admin}")
def confirmed_users(
    names,
    admin):
    for name in names:
        admin.append(name)
confirmed_users(usernames,admin)
print (f"\tAfter functon call admin = {admin}")

# Preventing a method from modifying a list
admin = []
print ("\nPreventing a function from modifying the list")
print (f"\tBefore functon call admin = {admin}")
confirmed_users(usernames, admin[:])
print (f"\tAfter function call admin = {admin}")

# Passing a arbitary number of Arguments
print ("\nPassing a arbitary number of arguments")
def make_burger(*things_under_bread):
    print ("\tBurger insides")
    for thing in things_under_bread: print(f"\t\t-{thing}")
print ("\tPassing a single argument")
make_burger("Tomoto")
print ("\n\tPassing a multiple argument")
make_burger("King size tikki","Baked Cheese","Sureign's spicy sauce ","Tomatoes","Onion","Red Sauce","Masala Fries")
