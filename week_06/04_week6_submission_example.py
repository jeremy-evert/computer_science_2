"""Week 6: submission-shaped example.

This file is intentionally small. It shows the pieces a student may submit:
1. an honest design decision,
2. code,
3. behavioral evidence,
4. a one-line World Bible entry,
5. a tiny AI accountability note when AI was used.
"""

import unittest


class Defender:
    def respond_to_intruder(self):
        raise NotImplementedError("Each kind of Defender needs its own response.")


class Guard(Defender):
    # STUDENT LEARNING:
    # "A Guard is a Defender" is an honest is-a statement.
    def respond_to_intruder(self):
        return "Guard walks toward the intruder."


class Turret(Defender):
    # STUDENT LEARNING:
    # The same operation can have subtype-specific behavior.
    def respond_to_intruder(self):
        return "Turret rotates and fires at the intruder."


class TestDefenderSubstitution(unittest.TestCase):
    def test_shared_operation_has_different_behavior(self):
        # STUDENT LEARNING:
        # Evidence matters. We call the same operation on both subtypes.
        guard_response = Guard().respond_to_intruder()
        turret_response = Turret().respond_to_intruder()

        self.assertNotEqual(guard_response, turret_response)
        self.assertEqual(guard_response, "Guard walks toward the intruder.")
        self.assertEqual(turret_response, "Turret rotates and fires at the intruder.")


# STUDENT LEARNING:
# The World Bible is not another essay. Record the design decision and evidence.
WORLD_BIBLE_ENTRY = (
    "Week 6: Guard and Turret remain Defender subtypes because both honestly "
    "support respond_to_intruder() with different behavior; unittest verifies it."
)


# STUDENT LEARNING:
# If AI helped, keep the receipt short: what it proposed, what you tested,
# and what you accepted or rejected.
AI_RECEIPT = (
    "AI proposed the Defender hierarchy. I ran the unittest myself and accepted "
    "the design because Guard and Turret both pass the is-a test."
)


if __name__ == "__main__":
    print("World Bible:", WORLD_BIBLE_ENTRY)
    print("AI receipt:", AI_RECEIPT)
    unittest.main()
