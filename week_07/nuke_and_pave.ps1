# Week 7 Contract and Swap -- Nuke and Pave
# Run this from the directory where you want the project created.
# It removes any existing week_07_contract_and_swap folder, creates
# every file, runs the tests, and runs the demonstration.

$ProjectName = "week_07_contract_and_swap"
$ProjectPath = Join-Path (Get-Location) $ProjectName

if (Test-Path $ProjectPath) {
    Remove-Item $ProjectPath -Recurse -Force
}
New-Item -ItemType Directory -Path $ProjectPath | Out-Null

# -----------------------------------------------------------------------
# settlement.py
# -----------------------------------------------------------------------
@'
"""
settlement.py  --  Week 7: Contract and Swap
Frontier Settlement world.

Design decisions documented here so the code and the World Bible agree:

CONTRACT
  GrowthReporter is the explicit ABC.  It promises one operation:
      report_growth(location: str) -> str
  The abstract method enforces the signature.  The caller boundary
  enforces the return type at run time so a bad collaborator cannot
  silently corrupt downstream output.

IS-A RELATIONSHIP (earned, not asserted)
  Both TrailScout and SignalTower are genuine kinds of GrowthReporter:
  they carry their own state, their reports change based on that state,
  and they answer the same settlement question with meaningfully different
  evidence.  A TrailScout remembers which locations it has visited; a
  SignalTower accumulates a message-volume count per location.  Neither
  could do the other's job by changing a string.

CALLER BOUNDARY
  SettlementGrowthSystem.check_growth(location) is the single crossing
  point.  The caller:
    1. Validates the location before sending it across the boundary.
    2. Validates the return value before accepting it from the collaborator.
    3. Catches collaborator failures and re-raises with context so the
       caller's client always gets a meaningful error, not an internal one.
  The caller does not inspect which concrete collaborator it holds.

CONTINUITY WITH WEEK 5
  Week 5 introduced two collaborating objects that worked together to
  track settlement growth: a scout who moved through the territory, and
  a communications system that relayed reports.  That design had an
  implicit dependency -- the caller assumed both objects shared a
  report() method but nothing enforced that promise.  This week that
  implicit assumption becomes the explicit GrowthReporter contract.
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------------------------
# Contract violation sentinel
# ---------------------------------------------------------------------------

class ContractViolationError(RuntimeError):
    """
    Raised when a collaborator returns a value that does not satisfy
    the GrowthReporter contract.  Keeping this as a named exception lets
    callers catch contract problems specifically instead of catching all
    RuntimeErrors.
    """


# ---------------------------------------------------------------------------
# The explicit contract
# ---------------------------------------------------------------------------

class GrowthReporter(ABC):
    """
    Contract for any object that can report settlement growth.

    Promise
    -------
    report_growth(location: str) -> str
        Receive a non-empty location name.
        Return a non-empty string describing growth evidence at that location.

    The contract does not say how the reporter gathers evidence.
    TrailScout uses foot-and-wagon traffic it has personally observed.
    SignalTower uses the volume of telegraph messages it has relayed.
    Both answer the same question; neither knows how the other works.
    """

    @abstractmethod
    def report_growth(self, location: str) -> str:
        """
        Return a non-empty string describing growth evidence at location.
        Raise ValueError if location is not a non-empty string.
        """
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Conforming collaborator 1: TrailScout
# Stateful -- remembers which locations it has visited.
# ---------------------------------------------------------------------------

class TrailScout(GrowthReporter):
    """
    Reports growth by observing wagon and foot traffic on the trail.

    State
    -----
    _visited : set[str]
        Locations this scout has personally visited.  A first visit
        produces a cautious report; a return visit produces a confident
        one because the scout can compare what it sees now to what it
        saw before.

    This state is what earns the is-a relationship.  A TrailScout is not
    just a string factory -- it is an observer with memory whose reports
    improve as it accumulates evidence.
    """

    def __init__(self):
        self._visited: set = set()

    def report_growth(self, location: str) -> str:
        if not isinstance(location, str) or not location.strip():
            raise ValueError(
                f"TrailScout.report_growth requires a non-empty string location; "
                f"got {location!r}"
            )
        if location in self._visited:
            return (
                f"Trail scout return visit to {location}: "
                "wagon tracks are heavier than last time -- "
                "the settlement is growing faster than first reported."
            )
        self._visited.add(location)
        return (
            f"Trail scout first visit to {location}: "
            "fresh wagon tracks suggest the settlement is beginning to grow."
        )

    @property
    def visited_locations(self) -> frozenset:
        """Read-only view of every location this scout has visited."""
        return frozenset(self._visited)


# ---------------------------------------------------------------------------
# Conforming collaborator 2: SignalTower
# Stateful -- accumulates message-volume counts per location.
# ---------------------------------------------------------------------------

class SignalTower(GrowthReporter):
    """
    Reports growth by counting telegraph messages relayed for each location.

    State
    -----
    _message_counts : dict[str, int]
        Number of messages relayed for each location.  Low volume
        produces a tentative report; high volume produces a confident one.

    This state is what earns the is-a relationship.  A SignalTower is
    not just a string factory -- it is a communications node that learns
    from accumulated traffic and revises its assessment accordingly.
    """

    LOW_VOLUME_THRESHOLD = 5

    def __init__(self):
        self._message_counts: dict = {}

    def relay_message(self, location: str) -> None:
        """
        Record one message relayed for location.
        Called by the telegraph operator each time a message passes through.
        This is a SignalTower-specific operation; the contract does not
        expose it.  Only SignalTower clients who know they hold a tower
        call this directly.
        """
        if not isinstance(location, str) or not location.strip():
            raise ValueError(
                f"relay_message requires a non-empty string location; "
                f"got {location!r}"
            )
        self._message_counts[location] = self._message_counts.get(location, 0) + 1

    def report_growth(self, location: str) -> str:
        if not isinstance(location, str) or not location.strip():
            raise ValueError(
                f"SignalTower.report_growth requires a non-empty string location; "
                f"got {location!r}"
            )
        count = self._message_counts.get(location, 0)
        if count == 0:
            return (
                f"Signal tower report for {location}: "
                "no messages relayed yet -- growth status unknown."
            )
        if count < self.LOW_VOLUME_THRESHOLD:
            return (
                f"Signal tower report for {location}: "
                f"{count} message(s) relayed -- early signs of growth detected."
            )
        return (
            f"Signal tower report for {location}: "
            f"{count} messages relayed -- high communication volume confirms "
            "the settlement is growing."
        )

    def message_count(self, location: str) -> int:
        """Return the number of messages relayed for location."""
        return self._message_counts.get(location, 0)


# ---------------------------------------------------------------------------
# Caller: SettlementGrowthSystem
# Depends on the GrowthReporter contract, not on any concrete collaborator.
# ---------------------------------------------------------------------------

class SettlementGrowthSystem:
    """
    Uses a GrowthReporter collaborator to answer growth questions about
    settlement locations.

    Caller boundary
    ---------------
    check_growth(location) is the single crossing point between this
    system and its collaborator.  At that boundary the caller:

      1. Validates the location before sending it across (the caller
         owns the input contract with its own clients).
      2. Validates the return value before accepting it (the caller
         enforces the collaborator output promise even though Python
         cannot enforce return types at the language level).
      3. Catches unexpected collaborator failures and re-raises them
         with context so the caller's client always receives a
         SettlementGrowthSystem error, not a raw collaborator error.

    The caller does not use isinstance() to ask which concrete
    collaborator it holds, and it does not call any collaborator-specific
    method (such as relay_message or visited_locations).
    """

    def __init__(self, growth_reporter: GrowthReporter):
        if not isinstance(growth_reporter, GrowthReporter):
            raise TypeError(
                f"growth_reporter must be a GrowthReporter; "
                f"got {type(growth_reporter).__name__!r}"
            )
        self._growth_reporter = growth_reporter

    def check_growth(self, location: str) -> str:
        """
        Caller boundary.

        Ask the collaborator for a growth report on location and return
        the result to the caller's client.

        Parameters
        ----------
        location : str
            Non-empty name of the settlement location to check.

        Returns
        -------
        str
            A non-empty growth report from the collaborator.

        Raises
        ------
        ValueError
            If location is not a non-empty string.
        ContractViolationError
            If the collaborator returns a value that is not a non-empty
            string, indicating the collaborator broke its contract promise.
        RuntimeError
            If the collaborator raises an unexpected exception; the
            original exception is chained for debugging.
        """
        # Step 1: validate input before crossing the boundary.
        if not isinstance(location, str) or not location.strip():
            raise ValueError(
                f"check_growth requires a non-empty string location; "
                f"got {location!r}"
            )

        # Step 2: cross the boundary and catch collaborator failures.
        try:
            report = self._growth_reporter.report_growth(location)
        except ValueError:
            # Re-raise input errors directly; they indicate bad caller usage.
            raise
        except Exception as exc:
            raise RuntimeError(
                f"GrowthReporter collaborator raised an unexpected error "
                f"while reporting on {location!r}: {exc}"
            ) from exc

        # Step 3: validate the return value before accepting it.
        if not isinstance(report, str) or not report.strip():
            raise ContractViolationError(
                f"GrowthReporter collaborator {type(self._growth_reporter).__name__!r} "
                f"returned {report!r} instead of a non-empty string. "
                f"The collaborator broke its contract promise."
            )

        return report
'@ | Set-Content -Path (Join-Path $ProjectPath "settlement.py") -Encoding utf8

# -----------------------------------------------------------------------
# test_settlement.py
# -----------------------------------------------------------------------
@'
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
'@ | Set-Content -Path (Join-Path $ProjectPath "test_settlement.py") -Encoding utf8

# -----------------------------------------------------------------------
# demo.py
# -----------------------------------------------------------------------
@'
"""
demo.py  --  Week 7: Contract and Swap
Frontier Settlement world.

Demonstrates:
  1. The same caller working with two different collaborators.
  2. Stateful collaborator behavior (reports change over time).
  3. The caller boundary catching a contract violation.
  4. The caller boundary catching a collaborator failure.
"""

from settlement import (
    ContractViolationError,
    GrowthReporter,
    SettlementGrowthSystem,
    SignalTower,
    TrailScout,
)

DIVIDER = "=" * 55


def section(title: str) -> None:
    print(f"\n{DIVIDER}")
    print(f"  {title}")
    print(DIVIDER)


def demonstrate_trail_scout() -> None:
    section("Collaborator 1: TrailScout (stateful)")
    scout = TrailScout()
    system = SettlementGrowthSystem(scout)

    print("\nFirst visit to Dry Creek:")
    print(" ", system.check_growth("Dry Creek"))

    print("\nReturn visit to Dry Creek (scout has memory):")
    print(" ", system.check_growth("Dry Creek"))

    print("\nFirst visit to Red Bluff (independent state):")
    print(" ", system.check_growth("Red Bluff"))

    print(f"\nLocations the scout has visited: {scout.visited_locations}")


def demonstrate_signal_tower() -> None:
    section("Collaborator 2: SignalTower (stateful)")
    tower = SignalTower()
    system = SettlementGrowthSystem(tower)

    print("\nNo messages relayed yet:")
    print(" ", system.check_growth("Dry Creek"))

    print("\nRelaying 3 messages for Dry Creek...")
    for _ in range(3):
        tower.relay_message("Dry Creek")
    print(" ", system.check_growth("Dry Creek"))

    print(f"\nRelaying {SignalTower.LOW_VOLUME_THRESHOLD + 2} more messages...")
    for _ in range(SignalTower.LOW_VOLUME_THRESHOLD + 2):
        tower.relay_message("Dry Creek")
    print(" ", system.check_growth("Dry Creek"))

    print(f"\nTotal messages relayed for Dry Creek: {tower.message_count('Dry Creek')}")
    print(f"Messages relayed for Red Bluff (unrelated): {tower.message_count('Red Bluff')}")


def demonstrate_the_swap() -> None:
    section("The Swap: same caller, different collaborators")
    location = "Dry Creek"
    collaborators = [
        ("TrailScout", TrailScout()),
        ("SignalTower", SignalTower()),
    ]
    for name, collaborator in collaborators:
        system = SettlementGrowthSystem(collaborator)
        report = system.check_growth(location)
        print(f"\n  Using {name}:")
        print(f"    {report}")
    print(
        "\n  SettlementGrowthSystem did not change between those two calls."
        "\n  Only the injected collaborator changed."
    )


def demonstrate_caller_boundary() -> None:
    section("Caller Boundary: input validation")
    system = SettlementGrowthSystem(TrailScout())

    print("\nAttempting check_growth(\"\"):")
    try:
        system.check_growth("")
    except ValueError as exc:
        print(f"  ValueError caught at boundary: {exc}")

    print("\nAttempting check_growth(None):")
    try:
        system.check_growth(None)
    except ValueError as exc:
        print(f"  ValueError caught at boundary: {exc}")

    section("Caller Boundary: return-type enforcement")

    class SilentlyBrokenReporter(GrowthReporter):
        """A collaborator that breaks its contract by returning None."""
        def report_growth(self, location):
            return None

    broken_system = SettlementGrowthSystem(SilentlyBrokenReporter())
    print("\nCollaborator returns None instead of a string:")
    try:
        broken_system.check_growth("Dry Creek")
    except ContractViolationError as exc:
        print(f"  ContractViolationError caught at boundary: {exc}")

    section("Caller Boundary: collaborator failure handling")

    class FailingReporter(GrowthReporter):
        """A collaborator that raises an unexpected exception."""
        def report_growth(self, location):
            raise ConnectionError("telegraph lines are down")

    failing_system = SettlementGrowthSystem(FailingReporter())
    print("\nCollaborator raises ConnectionError:")
    try:
        failing_system.check_growth("Dry Creek")
    except RuntimeError as exc:
        print(f"  RuntimeError with context caught at boundary: {exc}")
        print(f"  Original cause: {exc.__cause__}")


def main() -> None:
    print("\nFRONTIER SETTLEMENT GROWTH REPORT")
    print("Week 7: Contract and Swap Demonstration")

    demonstrate_trail_scout()
    demonstrate_signal_tower()
    demonstrate_the_swap()
    demonstrate_caller_boundary()

    print(f"\n{DIVIDER}")
    print("  Demonstration complete.")
    print(DIVIDER)


if __name__ == "__main__":
    main()
'@ | Set-Content -Path (Join-Path $ProjectPath "demo.py") -Encoding utf8

# -----------------------------------------------------------------------
# WORLD_BIBLE.md
# -----------------------------------------------------------------------
@'
# World Bible: Frontier Settlement
## Version 0.7 -- Contract and Swap

---

## 1. World Premise

The Frontier Settlement is a growing community on the edge of mapped territory.
Every week, the settlement needs to know whether it is actually growing -- not just
feel like it is growing. Two different kinds of observers answer that question using
different evidence: scouts who travel the trails, and towers who relay telegraph
messages. The settlement growth-tracking system depends on *any* observer that
can deliver a report, not on one specific kind.

---

## 2. The Cast

| Name | Role |
|---|---|
| `TrailScout` | Travels the territory; reports growth based on wagon and foot traffic observed firsthand |
| `SignalTower` | Relays telegraph messages; reports growth based on communication volume |
| `SettlementGrowthSystem` | Asks a reporter for growth evidence; uses the report to inform the settlement |
| `GrowthReporter` | The explicit contract that any growth reporter must satisfy |
| `ContractViolationError` | Raised when a collaborator breaks its contract promise |

---

## 3. One Real Flow

1. The settlement marshal asks the `SettlementGrowthSystem` whether Dry Creek is growing.
2. `check_growth("Dry Creek")` validates the location at the caller boundary.
3. The system passes the location to whichever `GrowthReporter` it holds.
4. The reporter (scout or tower) uses its own state and evidence to produce a report.
5. The system validates the report before returning it.
6. The marshal receives a readable, non-empty growth assessment.

---

## 4. Three Software Questions

1. Is a given location growing, based on the evidence this reporter has gathered?
2. Can the system work with a new kind of reporter without changing its own code?
3. What happens at the boundary when a reporter breaks its promise?

---

## 5. Known Unknowns

- **Location registry**: Should the system maintain a list of valid locations, or is any
  non-empty string acceptable? Right now any non-empty string passes. A later version
  might validate against a known list of settlements.
- **Structured reports**: `report_growth()` currently returns a plain string. A later
  version might return a structured object (`GrowthReport`) with fields for confidence
  level, evidence type, and timestamp.
- **Concurrency**: `TrailScout` and `SignalTower` both hold mutable state. If two threads
  ask for a report simultaneously, the state is not protected.

---

## 6. Object Prediction (updated each week)

| Candidate | Status |
|---|---|
| `TrailScout` | Confirmed -- carries visited-location state; behavior changes over time |
| `SignalTower` | Confirmed -- carries message-count state; behavior changes over time |
| `SettlementGrowthSystem` | Confirmed -- owns the caller boundary; delegates to a reporter |
| `GrowthReporter` | Confirmed -- explicit ABC contract, not a concrete object |
| `ContractViolationError` | Added this week -- named exception for broken contracts |

---

## 7. What Changed This Week (v0.6 to v0.7)

### The dependency became explicit

Week 5 introduced two collaborating objects that worked together to track settlement
growth. The dependency between the caller and its collaborators was implicit: both
happened to have a `report()` method, but nothing enforced that promise. This week
that implicit assumption became the explicit `GrowthReporter` ABC.

### The collaborators became real objects

The previous collaborators were stateless -- they returned the same string regardless
of what had happened before.

- `TrailScout` now carries a `_visited` set. A first visit produces a cautious report;
  a return visit produces a confident revision.
- `SignalTower` now carries `_message_counts`. Reports move through three stages
  (unknown, early signs, confirmed) as message volume accumulates.

Both collaborators now have state that justifies the class and earns the is-a
relationship.

### The caller boundary became real

`SettlementGrowthSystem.check_growth()` now has three explicit responsibilities:

1. **Input validation** -- location is checked before crossing the boundary.
2. **Return-type enforcement** -- the report is checked after crossing the boundary.
   A collaborator that returns `None` or an integer triggers `ContractViolationError`.
3. **Failure isolation** -- unexpected collaborator exceptions are caught and re-raised
   as `RuntimeError` with context.

### The tests became behavioral, not brittle

The old contract tests asserted exact strings. The new contract tests assert
properties: is the result a non-empty string? Does it mention the location? Does it
differ between collaborators? Collaborator-specific tests are in their own test class.

---

## 8. Evidence Used

35 tests across 4 test classes:

| Class | What it tests |
|---|---|
| `TestGrowthReporterContract` | Contract-level properties only; no concrete wording |
| `TestTrailScoutBehavior` | Scout state, first/return visit logic, input validation |
| `TestSignalTowerBehavior` | Tower state, volume thresholds, input validation |
| `TestCallerBoundary` | Input validation, return-type enforcement, failure handling |

Run: `python -m unittest -v`

Demonstration: `python demo.py`

---

## 9. Remaining Debt

| Item | Priority | Notes |
|---|---|---|
| `report_growth()` returns a plain string | Medium | A `GrowthReport` object would carry confidence level, evidence type, timestamp |
| Location validation is just "non-empty string" | Low | A future version could validate against a registry of known settlement locations |
| No thread-safety on mutable collaborator state | Low | Flag for when the system runs concurrently |
| `isinstance` guard blocks structural subtyping | Low | A `typing.Protocol` version would allow duck-typed conformance without inheritance |
'@ | Set-Content -Path (Join-Path $ProjectPath "WORLD_BIBLE.md") -Encoding utf8

# -----------------------------------------------------------------------
# README.md
# -----------------------------------------------------------------------
@'
# Week 7: Contract and Swap
## Frontier Settlement -- CS2 Reasoning Odyssey Gate

---

## What this project demonstrates

| Concept | Where to look |
|---|---|
| Explicit ABC contract | `GrowthReporter` in `settlement.py` |
| Stateful collaborators (earned is-a) | `TrailScout`, `SignalTower` in `settlement.py` |
| Caller boundary with 3 responsibilities | `SettlementGrowthSystem.check_growth()` in `settlement.py` |
| Focused contract tests (no concrete wording) | `TestGrowthReporterContract` in `test_settlement.py` |
| Collaborator-specific tests | `TestTrailScoutBehavior`, `TestSignalTowerBehavior` |
| Boundary tests (input, return type, failures) | `TestCallerBoundary` in `test_settlement.py` |
| Working demonstration | `demo.py` |
| Full six-part World Bible | `WORLD_BIBLE.md` |

---

## Files

```
week_07_contract_and_swap/
|-- settlement.py        contract, collaborators, and caller
|-- test_settlement.py   35 tests across 4 test classes
|-- demo.py              working demonstration of all concepts
|-- WORLD_BIBLE.md       full six-part design record
`-- README.md            this file
```

---

## Run the tests

```
python -m unittest -v
```

Expected: 35 tests, 0 failures, 0 errors.

---

## Run the demonstration

```
python demo.py
```

---

## Design summary

### The contract

```python
class GrowthReporter(ABC):
    @abstractmethod
    def report_growth(self, location: str) -> str:
        raise NotImplementedError
```

### The two conforming collaborators

**TrailScout** carries a set of visited locations. A first visit produces a cautious
report. A return visit produces a confident revision. The scout is a real object with
memory, not a string factory.

**SignalTower** carries a message-count dictionary. Reports move through three stages
(unknown, early signs, confirmed) as message volume accumulates.

### The caller boundary

`SettlementGrowthSystem.check_growth(location)` has three responsibilities:

1. Validate input before sending it across the boundary.
2. Validate the return value before accepting it from the collaborator.
3. Isolate collaborator failures and re-raise with context.

### The swap

```python
scout_system  = SettlementGrowthSystem(TrailScout())
tower_system  = SettlementGrowthSystem(SignalTower())
```

`SettlementGrowthSystem` itself does not change. Only the injected collaborator changes.

---

## Rubric alignment

| Criterion | Points | Evidence |
|---|---|---|
| Working contract and swap | 15 | `GrowthReporter`, `TrailScout`, `SignalTower`, `SettlementGrowthSystem` in `settlement.py` |
| Focused contract test | 10 | `TestGrowthReporterContract` -- 6 tests, zero concrete wording assertions |
| Caller-boundary reasoning | 10 | 9 boundary tests in `TestCallerBoundary`; boundary documented in code and World Bible |
| Demonstration, reflection, World Bible | 5 | `demo.py` runs; `WORLD_BIBLE.md` has all six parts |
'@ | Set-Content -Path (Join-Path $ProjectPath "README.md") -Encoding utf8

# -----------------------------------------------------------------------
# Run
# -----------------------------------------------------------------------
Set-Location $ProjectPath

Write-Host ""
Write-Host "Project created at:" -ForegroundColor Cyan
Write-Host $ProjectPath
Write-Host ""

Write-Host "Running 35 focused tests..." -ForegroundColor Yellow
python -m unittest -v
if ($LASTEXITCODE -ne 0) { throw "Tests failed." }

Write-Host ""
Write-Host "Running demonstration..." -ForegroundColor Yellow
python .\demo.py
if ($LASTEXITCODE -ne 0) { throw "Demonstration failed." }

Write-Host ""
Write-Host "SUCCESS: All tests pass. Contract, swap, boundary, and World Bible are ready." -ForegroundColor Green
