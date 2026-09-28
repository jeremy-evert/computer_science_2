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
