"""A small example of object-oriented programming with a Python class."""


class Pet:
    """Represent a pet with a name and a sound it can make."""

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        """Return this pet's greeting."""
        return f"{self.name} says {self.sound}!"


if __name__ == "__main__":
    my_pet = Pet("Milo", "meow")
    print(my_pet.speak())
