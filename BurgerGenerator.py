def make_burger(size, *toppings):
    print(f"\tMaking a {size}-deck Burger with the following topping:")
    for topping in toppings:
        print(f"\t\t-{topping}")
