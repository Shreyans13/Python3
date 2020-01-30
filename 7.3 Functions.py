# Mixing Positional and Arbitary Arguments
print("Mixing Positional and Arbitary Arguments")
def make_pizza(
    size,
    *topppings):
    print (f"\tMaking a {size}-inch pizza")
    for topping in topppings:
        print(f"\t\t-{topping}")
make_pizza(6,"Peperoni")
print()
make_pizza(10, "Paneer", "green Peppers", "Cheese crust")

# Using Arbitary Keyword Arguments
print("\nUsing Arbitary KeyWord Arguments")
def profile_builder(
    first,
    last,
    **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = profile_builder('SHREYANS', 'JAIN', skill = 'coder', field = 'Computer Science')

print(f"\tuser_profile = {user_profile}")

# Importing an entire module
print("\nImporting an entire module")
import BurgerGenerator
BurgerGenerator.make_burger(5,"Tomato")

# Importing Specific Function
print("\nImporting Specific Function")
from BurgerGenerator import make_burger
make_burger(10,"Potatoes","Chese Burst")

# Function Alias
print("\nGiving Module an alias")
import BurgerGenerator as bg
bg.make_burger(15,"Cheese Crust","Paneer Burst","")

# Importing all functions in a Module
from BurgerGenerator import *
make_burger(15,"Cheese Crust","Paneer Burst","")
make_burger(10,"Potatoes","Chese Burst")
make_burger(5,"Tomato")
