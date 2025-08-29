# Base class
class Character:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name} from {self.origin}.")

# Derived class with encapsulation and polymorphism
class Superhero(Character):
    def __init__(self, name, origin, power, alias):
        super().__init__(name, origin)
        self.__power = power  # Encapsulated attribute
        self.alias = alias

    def reveal_identity(self):
        print(f"My alias is {self.alias}, and my power is {self.__power}.")

    def use_power(self):
        print(f"{self.alias} uses {self.__power} to save the day!")

# Another derived class
class Villain(Character):
    def __init__(self, name, origin, evil_plan):
        super().__init__(name, origin)
        self.evil_plan = evil_plan

    def use_power(self):
        print(f"{self.name} executes their evil plan: {self.evil_plan}!")

# Example usage
hero = Superhero("Kal-El", "Krypton", "Flight", "Superman")
villain = Villain("Lex Luthor", "Earth", "World Domination")

hero.introduce()
hero.reveal_identity()
hero.use_power()

villain.introduce()
villain.use_power()