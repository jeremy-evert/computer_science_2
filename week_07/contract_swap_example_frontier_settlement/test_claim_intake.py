import unittest

from claim_intake import (
    ClaimIntake,
    TradePostIntake,
    WellBoardIntake,
    register_claim,
)


class TestClaimIntake(unittest.TestCase):

    def test_well_board_files_the_claim(self):
        intake = WellBoardIntake()

        result = register_claim(intake, "Merrow", 40)

        self.assertEqual(
            result,
            "Well Board record: Merrow claims 40 gal/day"
        )

    def test_trade_post_files_the_claim(self):
        intake = TradePostIntake()

        result = register_claim(intake, "Merrow", 40)

        self.assertEqual(
            result,
            "Trade Post ledger: Merrow - 40 gal/day allocation logged"
        )

    def test_register_claim_holds_the_contract_for_either_office(self):
        # The focused swap test: same caller, two different offices with
        # genuinely different record formats, one contract -- every
        # confirmation must name the claimant and the amount, regardless
        # of which office recorded it.
        claimant = "Merrow"
        gallons_per_day = 40
        intakes = [WellBoardIntake(), TradePostIntake()]

        for intake in intakes:
            with self.subTest(intake=type(intake).__name__):
                result = register_claim(intake, claimant, gallons_per_day)
                self.assertIn(claimant, result)
                self.assertIn(str(gallons_per_day), result)

    def test_register_claim_accepts_an_office_it_has_never_seen(self):
        # Guards against a caller that secretly special-cases WellBoard or
        # TradePost: a brand-new conforming office, opened after
        # register_claim was written, must work without editing it.
        class RoadDispatchIntake(ClaimIntake):
            def file_claim(self, claimant, gallons_per_day):
                return f"Road dispatch filing: {claimant} requests {gallons_per_day} gal/day"

        result = register_claim(RoadDispatchIntake(), "Old Tobin", 15)

        self.assertIn("Old Tobin", result)
        self.assertIn("15", result)

    def test_the_contract_is_enforced_not_just_documented(self):
        # What abc.ABC buys over a plain duck-typed class or
        # typing.Protocol: an office that forgets to implement
        # file_claim can't even be opened.
        class UnstaffedOffice(ClaimIntake):
            pass

        with self.assertRaises(TypeError):
            UnstaffedOffice()


if __name__ == "__main__":
    unittest.main(verbosity=2)
