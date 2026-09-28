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
