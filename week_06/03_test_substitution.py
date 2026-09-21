import unittest


# STUDENT LEARNING: A real project would normally import these classes from
# the application module. They are repeated here to keep this example focused.
class Defender:
    def respond_to_intruder(self):
        raise NotImplementedError("Each kind of defender needs its own response.")


class Guard(Defender):
    def respond_to_intruder(self):
        # STUDENT LEARNING: Returning a value makes behavior easy to check
        # automatically instead of requiring output-capture machinery.
        return "Guard walks toward the intruder."


class Turret(Defender):
    def respond_to_intruder(self):
        return "Turret rotates and fires at the intruder."


class TestDefenderSubstitution(unittest.TestCase):
    def test_subtypes_respond_differently(self):
        guard = Guard()
        turret = Turret()

        # STUDENT LEARNING: Both subtype objects support the same operation.
        guard_response = guard.respond_to_intruder()
        turret_response = turret.respond_to_intruder()

        # STUDENT LEARNING: Assertions turn a behavior claim into evidence
        # that Python verifies.
        self.assertNotEqual(guard_response, turret_response)
        self.assertEqual(guard_response, "Guard walks toward the intruder.")
        self.assertEqual(turret_response, "Turret rotates and fires at the intruder.")

        # STUDENT LEARNING: Test the shared contract and its results, not the
        # concrete type. This test is evidence that one shared operation can
        # produce subtype-specific behavior.


if __name__ == "__main__":
    unittest.main()
