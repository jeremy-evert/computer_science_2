"""Step 5: a swappable trading-post implementation with reserve rules."""

from step_01_values import SupplyQuote
from step_02_contracts import SupplySource
from step_03_validation import (
    validate_inventory,
    validate_item_name,
    validate_object_name,
)

class TradingPost(SupplySource):
    """
    A stateful independent supply source.

    The trading post keeps part of its inventory in reserve for local
    customers. It offers only the stock above that reserve.

    State owned by the trading post:

    - its name
    - current inventory
    - protected reserve quantity
    - number of quotes prepared
    - locations it has served

    This makes substitution meaningful. A warehouse and a trading post can
    receive the same request but make different promises because their rules
    and responsibilities differ.
    """

    def __init__(
        self,
        name: str,
        inventory: dict[str, int],
        reserve_quantity: int,
    ):
        self._name = validate_object_name(
            name,
            "Trading post",
        )
        self._inventory = validate_inventory(inventory)
        self._reserve_quantity = self._validate_reserve(
            reserve_quantity
        )
        self._quote_count = 0
        self._locations_served: set[str] = set()

    @property
    def name(self) -> str:
        return self._name

    @property
    def reserve_quantity(self) -> int:
        return self._reserve_quantity

    @property
    def quote_count(self) -> int:
        return self._quote_count

    @property
    def locations_served(self) -> frozenset:
        """
        Return an immutable view of locations served.
        """

        return frozenset(self._locations_served)

    def quantity_on_hand(self, item_name: str) -> int:
        """
        Return the total stock held by the trading post.
        """

        normalized_item = validate_item_name(item_name)
        return self._inventory.get(normalized_item, 0)

    def quantity_available_for_trade(self, item_name: str) -> int:
        """
        Return stock available after protecting the local reserve.
        """

        quantity_on_hand = self.quantity_on_hand(item_name)

        return max(
            0,
            quantity_on_hand - self._reserve_quantity,
        )

    def quote_supply(
        self,
        location: str,
        item_name: str,
        requested_quantity: int,
    ) -> SupplyQuote:
        """
        Report availability while protecting the local reserve.
        """

        self._quote_count += 1
        self._locations_served.add(location)

        available_quantity = self.quantity_available_for_trade(
            item_name
        )
        can_fulfill = available_quantity >= requested_quantity

        if can_fulfill:
            reason = (
                f"{self._name} can provide the requested {item_name} "
                "without using its protected local reserve."
            )
        else:
            reason = (
                f"{self._name} protects a reserve of "
                f"{self._reserve_quantity} units and can provide only "
                f"{available_quantity} units of {item_name}."
            )

        return SupplyQuote(
            source_name=self._name,
            item_name=item_name,
            requested_quantity=requested_quantity,
            available_quantity=available_quantity,
            can_fulfill=can_fulfill,
            reason=reason,
        )

    @staticmethod
    def _validate_reserve(reserve_quantity: int) -> int:
        if isinstance(reserve_quantity, bool) or not isinstance(
            reserve_quantity,
            int,
        ):
            raise TypeError(
                "Reserve quantity must be an integer."
            )

        if reserve_quantity < 0:
            raise ValueError(
                "Reserve quantity cannot be negative."
            )

        return reserve_quantity


# ============================================================
# CALLER AND CALLER BOUNDARY
# ============================================================
