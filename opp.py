class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self.__secret_identity = secret_identity  # Encapsulated attribute
        self.power_level = power_level

    def reveal_identity(self):
        return f"{self.name}'s secret identity is {self.__secret_identity} 🔍"

    def use_power(self):
        return f"{self.name} uses their power at level {self.power_level}! 💥"

    def move(self):  # Polymorphic method
        return f"{self.name} is running fast! 🏃"

    def __str__(self):
        return f"Hero: {self.name} | Power: {self.power_level}"

class FlyingHero(Superhero):
    def move(self):  # Polymorphism override
        return f"{self.name} is soaring through the sky! 🦸♂️✈️"

class TeleportingHero(Superhero):
    def move(self):  # Polymorphism override
        return f"{self.name} blinks out of existence! ⚡"

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):  # Polymorphic method
        pass

class Batmobile(Vehicle):
    def move(self):
        return f"{self.name} speeds through Gotham streets! 🦇🚗"

class Quinjet(Vehicle):
    def move(self):
        return f"{self.name} takes off vertically! ✈️"

# Demonstration
def showcase_movement(entity):
    print(entity.move())

# Create instances
hero1 = Superhero("Captain Python", "Alex", 9000)
hero2 = FlyingHero("Sky Guardian", "Jamie", 8500)
hero3 = TeleportingHero("Blink", "Taylor", 9200)
vehicle1 = Batmobile("Batmobile Mk. II")
vehicle2 = Quinjet("SHIELD Quinjet")

# Polymorphic behavior
print(hero1.reveal_identity())
showcase_movement(hero1)  # "Captain Python is running fast! 🏃"
showcase_movement(hero2)  # "Sky Guardian is soaring through the sky! 🦸♂️✈️"
showcase_movement(hero3)  # "Blink blinks out of existence! ⚡"
showcase_movement(vehicle1)  # "Batmobile Mk. II speeds through Gotham streets! 🦇🚗"
showcase_movement(vehicle2)  # "SHIELD Quinjet takes off vertically! ✈️"