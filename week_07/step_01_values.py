"""Step 1: the values and errors shared by the whole example."""

from dataclasses import dataclass

class ContractViolationError(RuntimeError):
    """
    Raised when a collaborator returns a value that breaks the contract.
    """


class SupplySourceError(RuntimeError):
    """
    Raised when a supply source fails while serving the caller.
    """


# ============================================================
# VALUES THAT CROSS THE CALLER BOUNDARY
# ============================================================


@dataclass(frozen=True)
class SupplyQuote:
    """
    Structured result promised by every supply source.

    A structured value is safer than returning an arbitrary string because
    the caller can inspect named fields and enforce the contract.
    """

    source_name: str
    item_name: str
    requested_quantity: int
    available_quantity: int
    can_fulfill: bool
    reason: str


@dataclass(frozen=True)
class SupplyDecision:
    """
    Final decision owned by the ExpeditionPlanner.

    The supply source provides evidence through a SupplyQuote.
    The planner owns the actual approval decision.
    """

    approved: bool
    location: str
    item_name: str
    requested_quantity: int
    approved_quantity: int
    source_name: str
    explanation: str

