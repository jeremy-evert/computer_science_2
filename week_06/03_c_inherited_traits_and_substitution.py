import unittest


# ============================================================
# APPLICATION CODE
# ============================================================

class Defender:
    """
    Defender is the parent class.

    Every Defender:
    1. has a name,
    2. starts with 100 health,
    3. can report whether it is active,
    4. must provide a response to an intruder.
    """

    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_active(self):
        return self.health > 0

    def respond_to_intruder(self):
        raise NotImplementedError(
            "Each kind of Defender needs its own response."
        )


class Guard(Defender):
    """
    Guard is a child of Defender.

    Guard inherits:
    - name
    - health
    - is_active()

    Guard provides its own version of:
    - respond_to_intruder()
    """

    def respond_to_intruder(self):
        return f"{self.name} walks toward the intruder."


class Turret(Defender):
    """
    Turret is another child of Defender.

    Turret inherits:
    - name
    - health
    - is_active()

    Turret provides its own version of:
    - respond_to_intruder()
    """

    def respond_to_intruder(self):
        return f"{self.name} rotates and fires at the intruder."


# ============================================================
# UNIT TESTS
# ============================================================

class TestDefenderInheritance(unittest.TestCase):

    def setUp(self):
        """
        setUp() runs before every test.

        It creates fresh objects so one test does not accidentally
        change the objects used by another test.
        """

        self.guard = Guard("Marshal Ada")
        self.turret = Turret("North Tower")

    def test_guard_is_a_defender(self):
        """
        A Guard is a Defender.
        """

        self.assertIsInstance(self.guard, Defender)

    def test_turret_is_a_defender(self):
        """
        A Turret is a Defender.
        """

        self.assertIsInstance(self.turret, Defender)

    def test_children_inherit_name(self):
        """
        Defender creates the name attribute.

        Guard and Turret do not define their own __init__ methods,
        so they inherit Defender.__init__().
        """

        self.assertEqual(self.guard.name, "Marshal Ada")
        self.assertEqual(self.turret.name, "North Tower")

    def test_children_inherit_starting_health(self):
        """
        Every Defender starts with 100 health.

        This parent guarantee is also true for both children.
        """

        self.assertEqual(self.guard.health, 100)
        self.assertEqual(self.turret.health, 100)

    def test_children_inherit_is_active(self):
        """
        Guard and Turret do not define is_active().

        They can still call it because they inherit it from Defender.
        """

        self.assertTrue(self.guard.is_active())
        self.assertTrue(self.turret.is_active())

    def test_inherited_is_active_method_can_become_false(self):
        """
        The parent's is_active() rule remains true for both children:

        health greater than 0 means active.
        health equal to 0 means not active.
        """

        self.guard.health = 0
        self.turret.health = 0

        self.assertFalse(self.guard.is_active())
        self.assertFalse(self.turret.is_active())

    def test_both_children_support_shared_operation(self):
        """
        Both child objects support the operation promised by Defender.
        """

        self.assertTrue(
            callable(self.guard.respond_to_intruder)
        )

        self.assertTrue(
            callable(self.turret.respond_to_intruder)
        )

    def test_guard_provides_guard_behavior(self):
        """
        Guard overrides the parent operation with Guard behavior.
        """

        result = self.guard.respond_to_intruder()

        self.assertEqual(
            result,
            "Marshal Ada walks toward the intruder."
        )

    def test_turret_provides_turret_behavior(self):
        """
        Turret overrides the parent operation with Turret behavior.
        """

        result = self.turret.respond_to_intruder()

        self.assertEqual(
            result,
            "North Tower rotates and fires at the intruder."
        )

    def test_subtypes_respond_differently(self):
        """
        The same operation produces different subtype behavior.

        This is polymorphism.
        """

        guard_response = self.guard.respond_to_intruder()
        turret_response = self.turret.respond_to_intruder()

        self.assertNotEqual(
            guard_response,
            turret_response
        )

    def test_defenders_can_be_used_in_one_collection(self):
        """
        Guard and Turret can both be placed in a collection of
        Defenders and receive the same operation.

        The loop does not need to ask which concrete type it has.
        """

        defenders = [
            self.guard,
            self.turret
        ]

        responses = []

        for defender in defenders:
            responses.append(
                defender.respond_to_intruder()
            )

        self.assertEqual(
            responses,
            [
                "Marshal Ada walks toward the intruder.",
                "North Tower rotates and fires at the intruder."
            ]
        )

    def test_parent_requires_children_to_supply_response(self):
        """
        Defender promises that the operation exists, but the parent
        does not provide a finished response.

        A child must override respond_to_intruder().
        """

        defender = Defender("Unnamed Defender")

        with self.assertRaises(NotImplementedError):
            defender.respond_to_intruder()


# ============================================================
# RUN THE TESTS
# ============================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)