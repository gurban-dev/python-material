# Objective:
# To understand class inheritance.

# Python classes inherit from the built-in object class by default.
class Animal(object):
    # Writing a constructor method is not mandatory.

    # If one is not written, the class automatically inherits
    # one from the default parent class (object).

    def __init__(self, species):
        self.species = species

        print("Animal constructor invoked.\n")

    # Instance method because its first parameter is self.
    def eat(self):
        print("The animal is eating.\n")

    def sleep(self):
        print("The animal is sleeping.\n")


# The Animal class provides two methods:
# • eat()
# • sleep()

# Now imagine a Dog class is created.
# Dogs can eat and sleep, but they can also bark.

# Dog is inheriting from the Animal class.
# This means that a Dog object will have the functionality
# that exists in the Animal class.

# However, Animal will not have the functionality that Dog
# has.
class Dog(Animal):
    def __init__(self, species, neutered):
        # Invoke the constructor method that was defined in the
        # parent class, Animal and pass the parameter species to
        # it.
        super().__init__(species)

        self.neutered = neutered

    def bark(self):
        print("Woof!\n")

# Object of the Animal class.
animal = Animal(species="Anteater")

animal.eat()

# Invalid because the Animal class does not inherit from the
# Dog class.
# animal.bark()

# Instance of the Dog class.
dog = Dog("Caucasian Shepherd", neutered=True)

dog.eat()

dog.bark()