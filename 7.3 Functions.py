# Mixing Positional and Arbitary Arguments
print("Mixing Positional and Arbitary Arguments")
def make_pizza(size, *topppings):
    print (f"\tMaking a {size}-inch pizza")
    for topping in topppings:
        print(f"\t\t-{topping}")
make_pizza(6,"Peperoni")
print()
make_pizza(10, "Paneer", "green Peppers", "Cheese crust")

print()
print("Using Arbitary KeyWord Arguments")
def profile_builder(first, last, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info

user_profile = profile_builder('SHREYANS', 'JAIN', skill = 'coder', field = 'Computer Science')

print(f"\tuser_profile = {user_profile}")

# function modules
