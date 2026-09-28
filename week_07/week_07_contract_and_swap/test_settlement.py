"""
test_settlement.py  --  Week 7: Contract and Swap
Frontier Settlement world.

Test organisation
-----------------
Four test classes with distinct responsibilities:

  TestGrowthReporterContract
    Contract-level tests only.  Every test exercises both collaborators
    through the SettlementGrowthSystem caller.  No test reaches through
    the contract to inspect collaborator-specific wording or state.
    This is the focused contract test the rubric requires.

  TestTrailScoutBehavior
    Collaborator-specific tests for TrailScout.  These are allowed to
    call TrailScout methods directly because they are testing the
    collaborator's own behavior, not the contract.

  TestSignalTowerBehavior
    Collaborator-specific tests for SignalTower.  Same reasoning.

  TestCallerBoundary
    Tests for the caller boundary decisions: input validation, return-
    type enforcement, and collaborator failure handling.

Naming convention
-----------------
Every test name is a full sentence that describes the expected behavior.
A failing test name should read like a bug report.
"""

import unittest
from settlement import (
    ContractViolationError,
    GrowthReporter,
    SettlementGrowthSystem,
    SignalTower,
    TrailScout,
)


# ---------------------------------------------------------------------------
# Focused contract tests
# These tests prove the contract works.  They do NOT inspect collaborator-
# specific wording, state, or methods.  They only assert properties that
# the contract itself promises: non-empty string, mentions the location,
# differs between collaborators.
# ---------------------------------------------------------------------------

class TestGrowthReporterContract(unittest.TestCase):
    """
    Focused contract tests.

    The same caller (SettlementGrowthSystem) exercises both collaborators.
    No test reaches through the contract boundary to inspect concrete
    collaborator details.
    """

    def test_abstract_contract_cannot_be_instantiated_directly(self):
        """GrowthReporter cannot be used without a concrete implementation."""
        with self.assertRaises(TypeError):
            GrowthReporter()

    def test_both_collaborators_satisfy_the_contract(self):
        """TrailScout and SignalTower both conform to the GrowthReporter contract."""
        collaborators = [TrailScout(), SignalTower()]
        for collaborator in collaborators:
            with self.subTest(collaborator=type(collaborator).__name__):
                self.assertIsInstance(collaborator, GrowthReporter)

    def test_both_collaborators_return_a_non_empty_string_through_the_caller(self):
        """
        Each collaborator returns a non-empty string when called through
        SettlementGrowthSystem.  The test asserts the CONTRACT property
        (non-empty string) not the concrete wording.
        """
        collaborators = [TrailScout(), SignalTower()]
        for collaborator in collaborators:
            with self.subTest(collaborator=type(collaborator).__name__):
                system = SettlementGrowthSystem(collaborator)
                report = system.check_growth("Dry Creek")
                self.assertIsInstance(report, str)
                self.assertTrue(len(report) > 0)

    def test_both_collaborators_include_the_location_in_their_report(self):
        """
        Each collaborator report mentions the location that was requested.
        This is a behavioral property, not a wording assertion.
        """
        location = "Dry Creek"
        collaborators = [TrailScout(), SignalTower()]
        for collaborator in collaborators:
            with self.subTest(collaborator=type(collaborator).__name__):
                system = SettlementGrowthSystem(collaborator)
                report = system.check_growth(location)
                self.assertIn(location, report)

    def test_two_collaborators_produce_meaningfully_different_reports(self):
        """
        TrailScout and SignalTower produce different reports for the same
        location, demonstrating that the swap changes behavior.
        The test does not assert WHAT the difference is, only THAT it exists.
        """
        location = "Dry Creek"
        scout_system = SettlementGrowthSystem(TrailScout())
        tower_system = SettlementGrowthSystem(SignalTower())
        scout_report = scout_system.check_growth(location)
        tower_report = tower_system.check_growth(location)
        self.assertNotEqual(scout_report, tower_report)

    def test_swapping_the_collaborator_changes_the_report_without_changing_the_caller(self):
        """
        SettlementGrowthSystem itself does not change when its collaborator
        is swapped.  Only the injected object changes.
        """
        location = "Dry Creek"
        scout_system = SettlementGrowthSystem(TrailScout())
        tower_system = SettlementGrowthSystem(SignalTower())
        # Both are the same class -- the caller did not change.
        self.assertIs(type(scout_system), type(tower_system))
        # Their reports differ -- the collaborator did change.
        self.assertNotEqual(
            scout_system.check_growth(location),
            tower_system.check_growth(location),
        )

    def test_caller_rejects_an_object_that_does_not_satisfy_the_contract(self):
        """An object that does not inherit from GrowthReporter is rejected at construction."""
        class NotAReporter:
            def report_growth(self, location):
                return "I look like a reporter but I am not one."

        with self.assertRaises(TypeError):
            SettlementGrowthSystem(NotAReporter())


# ---------------------------------------------------------------------------
# TrailScout collaborator-specific tests
# ---------------------------------------------------------------------------

class TestTrailScoutBehavior(unittest.TestCase):
    """
    Collaborator-specific tests for TrailScout.
    These test the scout's own behavior, not the contract.
    """

    def setUp(self):
        self.scout = TrailScout()

    def test_first_visit_to_a_location_produces_a_cautious_report(self):
        """A TrailScout first visit produces an initial growth assessment."""
        report = self.scout.report_growth("Dry Creek")
        self.assertIn("first visit", report)
        self.assertIn("Dry Creek", report)

    def test_return_visit_produces_a_more_confident_report(self):
        """A TrailScout second visit to the same location produces a revised report."""
        self.scout.report_growth("Dry Creek")
        report = self.scout.report_growth("Dry Creek")
        self.assertIn("return visit", report)

    def test_first_and_return_visit_reports_differ(self):
        """The scout report changes between the first and second visit."""
        first = self.scout.report_growth("Dry Creek")
        second = self.scout.report_growth("Dry Creek")
        self.assertNotEqual(first, second)

    def test_scout_tracks_visited_locations(self):
        """The scout remembers every location it has visited."""
        self.scout.report_growth("Dry Creek")
        self.scout.report_growth("Red Bluff")
        self.assertIn("Dry Creek", self.scout.visited_locations)
        self.assertIn("Red Bluff", self.scout.visited_locations)

    def test_unvisited_location_is_not_in_visited_set(self):
        """A location the scout has not visited does not appear in visited_locations."""
        self.scout.report_growth("Dry Creek")
        self.assertNotIn("Red Bluff", self.scout.visited_locations)

    def test_scout_reports_independently_for_different_locations(self):
        """Visiting one location does not affect the report for a different location."""
        self.scout.report_growth("Dry Creek")
        report = self.scout.report_growth("Red Bluff")
        self.assertIn("first visit", report)

    def test_scout_raises_value_error_for_empty_location(self):
        """TrailScout raises ValueError when location is an empty string."""
        with self.assertRaises(ValueError):
            self.scout.report_growth("")

    def test_scout_raises_value_error_for_none_location(self):
        """TrailScout raises ValueError when location is None."""
        with self.assertRaises(ValueError):
            self.scout.report_growth(None)

    def test_scout_raises_value_error_for_whitespace_location(self):
        """TrailScout raises ValueError when location is only whitespace."""
        with self.assertRaises(ValueError):
            self.scout.report_growth("   ")


# ---------------------------------------------------------------------------
# SignalTower collaborator-specific tests
# ---------------------------------------------------------------------------

class TestSignalTowerBehavior(unittest.TestCase):
    """
    Collaborator-specific tests for SignalTower.
    These test the tower's own behavior, not the contract.
    """

    def setUp(self):
        self.tower = SignalTower()

    def test_no_messages_relayed_produces_unknown_status_report(self):
        """A SignalTower with no relayed messages reports growth status as unknown."""
        report = self.tower.report_growth("Dry Creek")
        self.assertIn("unknown", report)

    def test_low_message_volume_produces_early_signs_report(self):
        """A low volume of messages produces a cautious growth report."""
        for _ in range(3):
            self.tower.relay_message("Dry Creek")
        report = self.tower.report_growth("Dry Creek")
        self.assertIn("early signs", report)

    def test_high_message_volume_produces_confirmed_growth_report(self):
        """High message volume produces a confident growth confirmation."""
        for _ in range(SignalTower.LOW_VOLUME_THRESHOLD + 2):
            self.tower.relay_message("Dry Creek")
        report = self.tower.report_growth("Dry Creek")
        self.assertIn("confirms", report)

    def test_report_changes_as_message_volume_increases(self):
        """The tower report changes as more messages are relayed."""
        unknown_report = self.tower.report_growth("Dry Creek")
        self.tower.relay_message("Dry Creek")
        early_report = self.tower.report_growth("Dry Creek")
        self.assertNotEqual(unknown_report, early_report)

    def test_message_count_starts_at_zero(self):
        """A new tower has relayed zero messages for any location."""
        self.assertEqual(self.tower.message_count("Dry Creek"), 0)

    def test_relay_message_increments_count(self):
        """relay_message increments the count for the given location."""
        self.tower.relay_message("Dry Creek")
        self.tower.relay_message("Dry Creek")
        self.assertEqual(self.tower.message_count("Dry Creek"), 2)

    def test_message_counts_are_tracked_independently_per_location(self):
        """Messages for one location do not affect counts for another location."""
        self.tower.relay_message("Dry Creek")
        self.tower.relay_message("Dry Creek")
        self.assertEqual(self.tower.message_count("Red Bluff"), 0)

    def test_tower_raises_value_error_for_empty_location(self):
        """SignalTower raises ValueError when location is an empty string."""
        with self.assertRaises(ValueError):
            self.tower.report_growth("")

    def test_tower_raises_value_error_for_none_location(self):
        """SignalTower raises ValueError when location is None."""
        with self.assertRaises(ValueError):
            self.tower.report_growth(None)

    def test_relay_message_raises_value_error_for_empty_location(self):
        """relay_message raises ValueError when location is an empty string."""
        with self.assertRaises(ValueError):
            self.tower.relay_message("")


# ---------------------------------------------------------------------------
# Caller boundary tests
# ---------------------------------------------------------------------------

class TestCallerBoundary(unittest.TestCase):
    """
    Tests for the caller boundary in SettlementGrowthSystem.check_growth().

    The boundary has three responsibilities:
      1. Validate input before sending it to the collaborator.
      2. Validate the collaborator return value before accepting it.
      3. Catch and re-raise unexpected collaborator failures with context.
    """

    def test_caller_raises_value_error_for_empty_location(self):
        """check_growth raises ValueError when location is an empty string."""
        system = SettlementGrowthSystem(TrailScout())
        with self.assertRaises(ValueError):
            system.check_growth("")

    def test_caller_raises_value_error_for_none_location(self):
        """check_growth raises ValueError when location is None."""
        system = SettlementGrowthSystem(TrailScout())
        with self.assertRaises(ValueError):
            system.check_growth(None)

    def test_caller_raises_value_error_for_whitespace_location(self):
        """check_growth raises ValueError when location is only whitespace."""
        system = SettlementGrowthSystem(TrailScout())
        with self.assertRaises(ValueError):
            system.check_growth("   ")

    def test_caller_raises_value_error_for_integer_location(self):
        """check_growth raises ValueError when location is an integer."""
        system = SettlementGrowthSystem(TrailScout())
        with self.assertRaises(ValueError):
            system.check_growth(42)

    def test_caller_raises_contract_violation_error_when_collaborator_returns_none(self):
        """
        If a collaborator returns None instead of a string, the caller
        raises ContractViolationError rather than passing None upstream.
        """
        class NoneReturningReporter(GrowthReporter):
            def report_growth(self, location):
                return None

        system = SettlementGrowthSystem(NoneReturningReporter())
        with self.assertRaises(ContractViolationError):
            system.check_growth("Dry Creek")

    def test_caller_raises_contract_violation_error_when_collaborator_returns_integer(self):
        """
        If a collaborator returns an integer, the caller raises
        ContractViolationError rather than passing the integer upstream.
        """
        class IntReturningReporter(GrowthReporter):
            def report_growth(self, location):
                return 42

        system = SettlementGrowthSystem(IntReturningReporter())
        with self.assertRaises(ContractViolationError):
            system.check_growth("Dry Creek")

    def test_caller_raises_contract_violation_error_when_collaborator_returns_empty_string(self):
        """
        If a collaborator returns an empty string, the caller raises
        ContractViolationError because an empty report violates the
        readable string promise.
        """
        class EmptyStringReporter(GrowthReporter):
            def report_growth(self, location):
                return ""

        system = SettlementGrowthSystem(EmptyStringReporter())
        with self.assertRaises(ContractViolationError):
            system.check_growth("Dry Creek")

    def test_caller_wraps_unexpected_collaborator_exception_with_context(self):
        """
        If a collaborator raises an unexpected exception, the caller
        catches it and re-raises as RuntimeError with context.
        The original exception is chained so it is still available.
        """
        class CrashingReporter(GrowthReporter):
            def report_growth(self, location):
                raise ConnectionError("telegraph lines are down")

        system = SettlementGrowthSystem(CrashingReporter())
        with self.assertRaises(RuntimeError) as ctx:
            system.check_growth("Dry Creek")
        self.assertIsNotNone(ctx.exception.__cause__)

    def test_caller_does_not_swallow_value_errors_from_collaborator(self):
        """
        ValueError from a collaborator is re-raised directly because it
        indicates bad input from the caller client, not an internal fault.
        """
        class PickyReporter(GrowthReporter):
            def report_growth(self, location):
                raise ValueError("I only report on registered locations")

        system = SettlementGrowthSystem(PickyReporter())
        with self.assertRaises(ValueError):
            system.check_growth("Dry Creek")


if __name__ == "__main__":
    unittest.main(verbosity=2)
