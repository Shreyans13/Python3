print("If Statements")
print("\tList of cars")
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print("\t",car.upper())
    else:
        print("\t",car.title())

import random
requested_toppings = ({'pepperoni','cheese burst'},{'mushrooms','extra cheese'},{})[random.randint(0,2)]
print("\tAutomatic pizza generator")
if requested_toppings:
    if 'mushrooms' in requested_toppings:
        print("\tAdding mushrooms.")
    if 'pepperoni' in requested_toppings:
        print("\tAdding pepperoni.")
    if 'extra cheese' in requested_toppings:
        print("\tAdding extra cheese.")
    if 'cheese burst' in requested_toppings:
        print("\tAdding cheese burst.")
    print("\nFinished making your pizza!")
else:
    print("\tNo Pizza for you")

banned_users=['Shivam Kumar Singh']
user=input("\tEnter a user full name\n\t").title()
if user not in banned_users:
    print(f"\tHi,{user} you are welcome")
else:
    print("\tYou are banned. Contact headquarters for further removal")
age=int(input("\tEnter your age"))
if age < 14:
    print("\tIn eligible")
elif age < 18:
    print("\tStill not Eligible")
elif age == 20:
    print("\tEligible")
else:
    print("\tFuck Off")#no hard feelings
