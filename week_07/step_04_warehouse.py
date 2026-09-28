"""Step 4: the settlement-warehouse implementation of the contract."""

from step_01_values import SupplyQuote
from step_02_contracts import SupplySource
from step_03_validation import (
    validate_inventory,
    validate_item_name,
    validate_object_name,
    validate_positive_quantity,
)

class SettlementWarehouse(SupplySource):
    """
    A stateful supply source owned by the settlement.

    The warehouse can offer every unit that it currently holds.

    State owned by the warehouse:

    - its name
    - current inventory
    - locations for which it has prepared quotes
    - supplies it has issued

    This is a real object rather than a function in a costume because its
    behavior depends on state that persists and changes over time.
    """

    def __init__(self, name: str, inventory: dict[str, int]):
        self._name = validate_object_name(
            name,
            "Warehouse",
        )
        self._inventory = validate_inventory(inventory)
        self._quoted_locations: set[str] = set()
        self._completed_issues: list[tuple[str, str, int]] = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def quoted_locations(self) -> frozenset:
        """
        Return an immutable view of quoted locations.
        """

        return frozenset(self._quoted_locations)

    @property
    def completed_issues(self) -> tuple[tuple[str, str, int], ...]:
        """
        Return an immutable view of completed supply issues.
        """

        return tuple(self._completed_issues)

    def quantity_on_hand(self, item_name: str) -> int:
        """
        Return the current quantity of an item.
        """

        normalized_item = validate_item_name(item_name)
        return self._inventory.get(normalized_item, 0)

    def add_stock(self, item_name: str, quantity: int) -> None:
        """
        Add stock to the warehouse.
        """

        normalized_item = validate_item_name(item_name)
        validated_quantity = validate_positive_quantity(quantity)

        current_quantity = self._inventory.get(normalized_item, 0)
        self._inventory[normalized_item] = (
            current_quantity + validated_quantity
        )

    def issue_supply(
        self,
        location: str,
        item_name: str,
        quantity: int,
    ) -> None:
        """
        Remove issued supplies from inventory and record the issue.
        """

        if not isinstance(location, str):
            raise TypeError("Location must be a string.")

        normalized_location = location.strip()

        if not normalized_location:
            raise ValueError("Location must not be empty.")

        normalized_item = validate_item_name(item_name)
        validated_quantity = validate_positive_quantity(quantity)
        available_quantity = self.quantity_on_hand(normalized_item)

        if validated_quantity > available_quantity:
            raise ValueError(
                f"{self._name} cannot issue "
                f"{validated_quantity} units of {normalized_item}; "
                f"only {available_quantity} are available."
            )

        self._inventory[normalized_item] = (
            available_quantity - validated_quantity
        )

        self._completed_issues.append(
            (
                normalized_location,
                normalized_item,
                validated_quantity,
            )
        )

    def quote_supply(
        self,
        location: str,
        item_name: str,
        requested_quantity: int,
    ) -> SupplyQuote:
        """
        Report availability using the warehouse's current inventory.
        """

        self._quoted_locations.add(location)

        available_quantity = self.quantity_on_hand(item_name)
        can_fulfill = available_quantity >= requested_quantity

        if can_fulfill:
            reason = (
                f"{self._name} has enough {item_name} "
                "in settlement inventory."
            )
        else:
            reason = (
                f"{self._name} has only {available_quantity} units "
                f"of {item_name} in settlement inventory."
            )

        return SupplyQuote(
            source_name=self._name,
            item_name=item_name,
            requested_quantity=requested_quantity,
            available_quantity=available_quantity,
            can_fulfill=can_fulfill,
            reason=reason,
        )


# ============================================================
# SECOND CONFORMING COLLABORATOR
# ============================================================
