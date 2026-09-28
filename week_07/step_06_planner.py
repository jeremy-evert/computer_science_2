"""Step 6: the caller that uses a supply source through its contract."""

from step_01_values import (
    ContractViolationError,
    SupplyDecision,
    SupplyQuote,
    SupplySourceError,
)
from step_02_contracts import SupplySourceProtocol
from step_03_validation import validate_item_name, validate_positive_quantity

class ExpeditionPlanner:
    """
    Caller that depends on the SupplySource promise.

    The caller boundary is:

        evaluate_supply_request(
            location,
            item_name,
            requested_quantity,
        )

    The caller performs real work at this boundary:

    1. It validates input from the outside world.
    2. It asks the collaborator for a quote.
    3. It adds context if the collaborator fails.
    4. It verifies that the returned object satisfies the contract.
    5. It approves or declines the request.
    6. It records the completed decision.

    The planner does not need warehouse-specific or trading-post-specific
    branches.
    """

    def __init__(self, supply_source: SupplySourceProtocol):
        quote_method = getattr(
            supply_source,
            "quote_supply",
            None,
        )

        if not callable(quote_method):
            raise TypeError(
                "supply_source must provide a callable "
                "quote_supply() method."
            )

        self._supply_source = supply_source
        self._last_decision: SupplyDecision | None = None
        self._decision_history: list[SupplyDecision] = []

    @property
    def last_decision(self) -> SupplyDecision | None:
        return self._last_decision

    @property
    def decision_history(self) -> tuple[SupplyDecision, ...]:
        return tuple(self._decision_history)

    def evaluate_supply_request(
        self,
        location: str,
        item_name: str,
        requested_quantity: int,
    ) -> SupplyDecision:
        """
        Validate a request, consult the collaborator, enforce the contract,
        and create the final decision.
        """

        validated_location = self._validate_location(location)
        validated_item = validate_item_name(item_name)
        validated_quantity = validate_positive_quantity(
            requested_quantity
        )

        try:
            quote = self._supply_source.quote_supply(
                validated_location,
                validated_item,
                validated_quantity,
            )
        except Exception as error:
            raise SupplySourceError(
                f"Supply check failed for "
                f"{validated_location}: {error}"
            ) from error

        self._enforce_quote_contract(
            quote=quote,
            location=validated_location,
            item_name=validated_item,
            requested_quantity=validated_quantity,
        )

        if quote.can_fulfill:
            decision = SupplyDecision(
                approved=True,
                location=validated_location,
                item_name=validated_item,
                requested_quantity=validated_quantity,
                approved_quantity=validated_quantity,
                source_name=quote.source_name,
                explanation=(
                    f"Request approved using "
                    f"{quote.source_name}. {quote.reason}"
                ),
            )
        else:
            decision = SupplyDecision(
                approved=False,
                location=validated_location,
                item_name=validated_item,
                requested_quantity=validated_quantity,
                approved_quantity=0,
                source_name=quote.source_name,
                explanation=(
                    f"Request declined using "
                    f"{quote.source_name}. {quote.reason}"
                ),
            )

        self._last_decision = decision
        self._decision_history.append(decision)

        return decision

    @staticmethod
    def _validate_location(location: str) -> str:
        if not isinstance(location, str):
            raise TypeError("Location must be a string.")

        normalized_location = location.strip()

        if not normalized_location:
            raise ValueError("Location must not be empty.")

        return normalized_location

    @staticmethod
    def _enforce_quote_contract(
        quote: object,
        location: str,
        item_name: str,
        requested_quantity: int,
    ) -> None:
        """
        Enforce the collaborator promise at the actual boundary crossing.
        """

        if not isinstance(quote, SupplyQuote):
            raise ContractViolationError(
                "quote_supply() must return a SupplyQuote; "
                f"received {type(quote).__name__}."
            )

        if (
            not isinstance(quote.source_name, str)
            or not quote.source_name.strip()
        ):
            raise ContractViolationError(
                "SupplyQuote.source_name must be a non-empty string."
            )

        if quote.item_name != item_name:
            raise ContractViolationError(
                "SupplyQuote.item_name does not match "
                "the requested item."
            )

        if quote.requested_quantity != requested_quantity:
            raise ContractViolationError(
                "SupplyQuote.requested_quantity does not match "
                "the requested quantity."
            )

        if (
            isinstance(quote.available_quantity, bool)
            or not isinstance(quote.available_quantity, int)
        ):
            raise ContractViolationError(
                "SupplyQuote.available_quantity must be an integer."
            )

        if quote.available_quantity < 0:
            raise ContractViolationError(
                "SupplyQuote.available_quantity cannot be negative."
            )

        if not isinstance(quote.can_fulfill, bool):
            raise ContractViolationError(
                "SupplyQuote.can_fulfill must be Boolean."
            )

        expected_can_fulfill = (
            quote.available_quantity >= requested_quantity
        )

        if quote.can_fulfill != expected_can_fulfill:
            raise ContractViolationError(
                "SupplyQuote.can_fulfill contradicts the reported "
                f"availability for {location}."
            )

        if (
            not isinstance(quote.reason, str)
            or not quote.reason.strip()
        ):
            raise ContractViolationError(
                "SupplyQuote.reason must be a non-empty string."
            )


# ============================================================
# REUSABLE CONTRACT TESTS
# ============================================================

