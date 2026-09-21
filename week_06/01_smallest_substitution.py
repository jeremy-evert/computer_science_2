class Defender:
    # STUDENT LEARNING: Every Defender supports this shared operation.
    def respond_to_intruder(self):
        raise NotImplementedError("Each kind of defender needs its own response.")


class Guard(Defender):
    # STUDENT LEARNING: A Guard is honestly a kind of Defender, so inheritance
    # matches the model instead of being used only to reuse code.
    def respond_to_intruder(self):
        print("Guard walks toward the intruder.")


class Turret(Defender):
    # STUDENT LEARNING: A Turret is also a kind of Defender, but it responds
    # differently because a turret has different behavior.
    def respond_to_intruder(self):
        print("Turret rotates and fires at the intruder.")


# STUDENT LEARNING: Similar code alone does not justify inheritance. The child
# must honestly be a kind of the parent.
defenders = [Guard(), Turret()]

# STUDENT LEARNING: The client sends the same call to every object in the
# collection and gets each subtype's result, with no type-checking required.
for defender in defenders:
    defender.respond_to_intruder()
