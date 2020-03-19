# Object Oriented Programming
# Making object from class is called instantiation.
print("Object Oriented Programming - Class")
class Dog(object):
    """docstring for Dog."""

    def __init__(self, name, age):
        super(Dog, self).__init__()
        self.name = name
        self.age = age
    def sit(self):
        print(f"\t{self.name} is now sitting.")
    def roll_over(self):
        print(f"\t{self.name} is now rolling over")

my_dog = Dog('Leo', 3)
print(f"\tMy dog is {my_dog.name}.")
print(f"\tMy dog is {my_dog.age} is years old.")
my_dog.roll_over()
my_dog.sit()

print()

your_dog = Dog('Rusty', 5)
print(f"\tMy dog is {your_dog.name}.")
print(f"\tMy dog is {your_dog.age} is years old.")
your_dog.roll_over()
your_dog.sit()
