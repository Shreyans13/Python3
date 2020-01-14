import random
requested_toppings = ({'pepperoni','cheese burst'},{'mushrooms','extra cheese'},{})[random.randint(0,2)]
print("\tAutomatic pizza generator")
print(requested_toppings)
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
    
