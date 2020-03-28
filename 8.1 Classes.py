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


# Working with classes and instance

class Car(object):
	"""A simple attempt to represent a car."""
	def __init__(self, make , model ,year):
		"""Initialize attributes to describe a car"""
		# super(Car, self).__init__()
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name"""
		return f"{self.year} {self.make} {self.model}".title()
	
	def read_odometer(self):
		"""Print a statement showing car`s mileage """
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You cant! roll back an odometer!")

	def incrememt_odometer(self, miles):
		"""Add the given amount to odometer reading"""
		self.odometer_reading += miles

my_new_car = Car('audi','a13',2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(130)
my_new_car.read_odometer()

my_new_car.incrememt_odometer(20)
my_new_car.read_odometer()
