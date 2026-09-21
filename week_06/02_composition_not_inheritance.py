class Key:
    def __init__(self, value):
        self.value = value


class Lock:
    def __init__(self, key_value):
        self.key_value = key_value

    def opens_with(self, key):
        return key.value == self.key_value


class Vault:
    def __init__(self, lock):
        # STUDENT LEARNING: Ask "is-a?" before inheriting. A Vault is not a
        # Keyholder, so code such as class Vault(Keyholder) would be dishonest.
        # Vault has-a Lock. Guard is-a Defender in the first example.
        self.lock = lock

    def open(self, key):
        if self.lock.opens_with(key):
            print("The key fits. Vault opened.")


class Keyholder:
    def __init__(self, key):
        # STUDENT LEARNING: Keyholder has-a Key, so composition represents the
        # relationship more honestly than inventing a shared parent class.
        self.key = key

    def open_vault(self, vault):
        # STUDENT LEARNING: Working together does not make two objects members
        # of the same family. The Keyholder and Vault collaborate by calling
        # each other's operations while staying different kinds of things.
        vault.open(self.key)


# STUDENT LEARNING: Keep responsibilities separate: the Vault owns the Lock,
# and the Keyholder owns the Key. Neither object needs to become the other.
vault = Vault(Lock("blue"))
keyholder = Keyholder(Key("blue"))
keyholder.open_vault(vault)
