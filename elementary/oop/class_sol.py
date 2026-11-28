class Country:
    def __init__(self, name, population, population_unit):
        self.name = name

        # Note that the population is in millions.
        # E.g. 9.82 means 9.82 million
        self.population = population

        self.population_unit = population_unit

    def increase_pop(self, change):
        self.population += change

    def decrease_pop(self, change):
        self.population -= change

    def get_name(self):
        return self.name

    def get_population(self):
        return f"{self.population} {self.population_unit}"

# Instance of the Country class.
greece = Country("Greece", 9.88, "million")

# Above, there were positional arguments provided.
# They are called positional argument since the names of the
# parameters are not provided.

# Keyword arguments can be provided as well.
# A keyword argument contains both the parameter and the argument.
uk = Country(
    name="UK",
    population=70.1,
    population_unit="million"
)

print(f"greece.get_name(): {greece.get_name()}\n"
      f"greece.get_population(): {greece.get_population()}")

print(f"\nuk.get_name(): {uk.get_name()}\n"
      f"uk.get_population(): {uk.get_population()}")