import unittest

from evidence_logger import (
    EvidenceLogger,
    FieldUnitLogger,
    RecordsDivisionLogger,
    intake_evidence,
)


class TestEvidenceLogger(unittest.TestCase):

    def test_records_division_logs_the_item(self):
        logger = RecordsDivisionLogger()

        result = intake_evidence(logger, "EV-104", "sealed envelope, unopened")

        self.assertEqual(
            result,
            "CASE RECORDS: item EV-104 logged - sealed envelope, unopened"
        )

    def test_field_unit_logs_the_item(self):
        logger = FieldUnitLogger()

        result = intake_evidence(logger, "EV-104", "sealed envelope, unopened")

        self.assertEqual(
            result,
            "[FIELD REPORT #EV-104] sealed envelope, unopened (pending records review)"
        )

    def test_intake_evidence_holds_the_contract_for_either_logger(self):
        # The focused swap test: same caller, two genuinely different
        # record formats (Records Division vs. a field unit), one
        # contract -- every log entry must name the item id and the
        # description, regardless of which format wrote it.
        item_id = "EV-104"
        description = "sealed envelope, unopened"
        loggers = [RecordsDivisionLogger(), FieldUnitLogger()]

        for logger in loggers:
            with self.subTest(logger=type(logger).__name__):
                result = intake_evidence(logger, item_id, description)
                self.assertIn(item_id, result)
                self.assertIn(description, result)

    def test_intake_evidence_accepts_a_logger_it_has_never_seen(self):
        # Guards against a caller that secretly special-cases Records
        # Division or a field unit: a brand-new conforming logger, added
        # after intake_evidence was written, must work without editing it.
        class NightShiftLogger(EvidenceLogger):
            def log_intake(self, item_id, description):
                return f"(overnight intake) #{item_id}: {description}"

        result = intake_evidence(NightShiftLogger(), "EV-207", "torn receipt")

        self.assertIn("EV-207", result)
        self.assertIn("torn receipt", result)

    def test_the_contract_is_enforced_not_just_documented(self):
        # What abc.ABC buys over a plain duck-typed class or
        # typing.Protocol: a division that forgets to implement
        # log_intake can't even be constructed -- the gap can't slip
        # through to a case file later.
        class UnverifiedDivision(EvidenceLogger):
            pass

        with self.assertRaises(TypeError):
            UnverifiedDivision()


if __name__ == "__main__":
    unittest.main(verbosity=2)
