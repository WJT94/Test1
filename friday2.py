class Character:
    def __init__(self, name, adventurer_class):
        self.name = name
        self.alive = True


class Human(Character):
    health = 10
    eyes = 2
    hands = 2

    def say_hello(self):
        print(f"{self.name} says, \"Hello!\"")


class Elf(Character):
    health = 10
    eyes = 2
    hands = 2

    def say_hello(self):
        print(f"{self.name} sings, \"Aiya.\"")


class Beholder(Character):
    health = 20
    eyes = 10
    hands = 0

    def say_hello(self):
        print(f"{self.name} growls in an incomprehensible tongue.")


new_character = Human("Anne")
new_elf = Elf("Legolas")
new_beholder = Beholder("As'df")

print(f"{new_character.name} has {new_character.eyes} eyes and {new_character.hands} hands.")

# Have each character say hello
new_character.say_hello()
new_elf.say_hello()
new_beholder.say_hello()

# Remove one of the beholder's eyes
print(f"{new_beholder.name} has {new_beholder.eyes} eyes.")
new_beholder.eyes -= 1
print(f"{new_beholder.name} has lost an eye! They now have {new_beholder.eyes}.")