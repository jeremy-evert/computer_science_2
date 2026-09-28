"""Step 2: the explicit supply-source promise."""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

from step_01_values import SupplyQuote

class SupplySource(ABC):
    """
    Explicit nominal contract for a supply source.

    A supply source promises that it can examine a request and return a
    SupplyQuote.

    SettlementWarehouse and TradingPost are both genuine kinds of supply
    sources. They satisfy the same operation but use different state and
    different rules.
    """

    @abstractmethod
    def quote_supply(
        self,
        location: str,
        item_name: str,
        requested_quantity: int,
    ) -> SupplyQuote:
        """
        Return a SupplyQuote for a validated supply request.
        """
        raise NotImplementedError


# ============================================================
# OPTIONAL PROTOCOL COMPARISON
# ============================================================


@runtime_checkable
class SupplySourceProtocol(Protocol):
    """
    Structural version of the same promise.

    An object can satisfy this Protocol by providing quote_supply(), even if
    it does not inherit from SupplySource.

    The ABC is the explicit teaching example. The Protocol demonstrates that
    Python can also recognize a contract by behavior rather than ancestry.
    """

    def quote_supply(
        self,
        location: str,
        item_name: str,
        requested_quantity: int,
    ) -> SupplyQuote:
        ...


# ============================================================
# SHARED VALIDATION HELPERS
# ============================================================

