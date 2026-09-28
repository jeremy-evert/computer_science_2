import unittest

from subsystem_reporter import (
    LegacySensorArray,
    NextGenSensorArray,
    SubsystemReporter,
    log_subsystem_status,
)


class TestSubsystemReporter(unittest.TestCase):

    def test_legacy_sensor_array_reports_status(self):
        reporter = LegacySensorArray()

        result = log_subsystem_status(reporter, "life support")

        self.assertEqual(
            result,
            "LOG :: life support :: NOMINAL"
        )

    def test_next_gen_sensor_array_reports_status(self):
        reporter = NextGenSensorArray()

        result = log_subsystem_status(reporter, "life support")

        self.assertEqual(
            result,
            "{'subsystem': 'life support', 'status': 'nominal'}"
        )

    def test_log_subsystem_status_holds_the_contract_for_either_generation(self):
        # The focused swap test: same caller, two subsystems built to
        # different eras' interface standards (a flat log line vs. a
        # structured reading), one contract -- every status report must
        # name the subsystem, regardless of which generation produced it.
        subsystem_name = "life support"
        reporters = [LegacySensorArray(), NextGenSensorArray()]

        for reporter in reporters:
            with self.subTest(reporter=type(reporter).__name__):
                result = log_subsystem_status(reporter, subsystem_name)
                self.assertIn(subsystem_name, result)

    def test_log_subsystem_status_accepts_a_reporter_it_has_never_seen(self):
        # Guards against a caller that secretly special-cases the legacy
        # or next-gen array: a brand-new conforming reporter, installed
        # after log_subsystem_status was written, must work without
        # editing it.
        class ExperimentalSensorPod(SubsystemReporter):
            def report_status(self, subsystem_name):
                return f"<telemetry subsystem={subsystem_name!r} state=nominal/>"

        result = log_subsystem_status(ExperimentalSensorPod(), "navigation")

        self.assertIn("navigation", result)

    def test_the_contract_is_enforced_not_just_documented(self):
        # What abc.ABC buys over a plain duck-typed class or
        # typing.Protocol: a subsystem reporter that forgets to
        # implement report_status can't even be installed.
        class UncalibratedArray(SubsystemReporter):
            pass

        with self.assertRaises(TypeError):
            UncalibratedArray()


if __name__ == "__main__":
    unittest.main(verbosity=2)
