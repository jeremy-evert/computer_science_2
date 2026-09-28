"""
CS2 Week 7: Contract and Swap
File: class_example.py

This single-file example explores:

1. Test-Driven Development with unittest
2. Stateful collaborating objects
3. A genuine is-a relationship
4. An explicit ABC contract
5. Two swappable implementations
6. A meaningful caller boundary
7. Runtime contract enforcement
8. Failure handling
9. Optional Protocol comparison
10. A concise World Bible entry

Run everything:

    python .\class_example.py

Run tests only:

    python .\class_example.py test

Run the demonstration only:

    python .\class_example.py demo

Show the World Bible only:

    python .\class_example.py bible
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
import sys
import unittest
from typing import Protocol, runtime_checkable


# ============================================================
# DOMAIN ERRORS
# ============================================================


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


# ============================================================
# EXPLICIT CONTRACT
# ============================================================


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


def normalize_item_name(item_name: str) -> str:
    """
    Normalize an item name for inventory lookups.
    """

    return item_name.strip().lower()


def validate_object_name(name: str, object_description: str) -> str:
    """
    Validate and normalize the name of a domain object.
    """

    if not isinstance(name, str):
        raise TypeError(f"{object_description} name must be a string.")

    normalized_name = name.strip()

    if not normalized_name:
        raise ValueError(
            f"{object_description} name must not be empty."
        )

    return normalized_name


def validate_item_name(item_name: str) -> str:
    """
    Validate and normalize an inventory item name.
    """

    if not isinstance(item_name, str):
        raise TypeError("Item name must be a string.")

    normalized_item = normalize_item_name(item_name)

    if not normalized_item:
        raise ValueError("Item name must not be empty.")

    return normalized_item


def validate_positive_quantity(quantity: int) -> int:
    """
    Require a positive integer quantity.

    Boolean values are rejected because bool is technically a subclass of int
    in Python, but True and False are not sensible supply quantities here.
    """

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_inventory(inventory: dict[str, int]) -> dict[str, int]:
    """
    Validate inventory and return a normalized copy.
    """

    if not isinstance(inventory, dict):
        raise TypeError("Inventory must be provided as a dictionary.")

    validated_inventory: dict[str, int] = {}

    for item_name, quantity in inventory.items():
        normalized_item = validate_item_name(item_name)

        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError(
                f"Inventory quantity for {normalized_item} "
                "must be an integer."
            )

        if quantity < 0:
            raise ValueError(
                f"Inventory quantity for {normalized_item} "
                "cannot be negative."
            )

        validated_inventory[normalized_item] = quantity

    return validated_inventory


# ============================================================
# FIRST CONFORMING COLLABORATOR
# ============================================================


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
    def quoted_locations(self) -> frozenset"""
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
    def locations_served(self) -> frozenset"""
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


class SupplySourceContractTests:
    """
    Reusable behavioral contract tests.

    A concrete TestCase supplies make_source(). The same tests are then run
    against each implementation.

    These tests focus on the shared promise. They do not assert exact prose or
    reach into implementation-specific state.
    """

    def make_source(self):
        raise NotImplementedError

    def test_contract_returns_a_supply_quote(self):
        source = self.make_source()

        quote = source.quote_supply(
            location="North Ridge",
            item_name="water",
            requested_quantity=3,
        )

        self.assertIsInstance(quote, SupplyQuote)

    def test_contract_preserves_request_information(self):
        source = self.make_source()

        quote = source.quote_supply(
            location="North Ridge",
            item_name="water",
            requested_quantity=3,
        )

        self.assertEqual(quote.item_name, "water")
        self.assertEqual(quote.requested_quantity, 3)

    def test_contract_reports_nonnegative_availability(self):
        source = self.make_source()

        quote = source.quote_supply(
            location="North Ridge",
            item_name="water",
            requested_quantity=3,
        )

        self.assertIsInstance(
            quote.available_quantity,
            int,
        )
        self.assertGreaterEqual(
            quote.available_quantity,
            0,
        )

    def test_contract_identifies_source_and_explains_result(self):
        source = self.make_source()

        quote = source.quote_supply(
            location="North Ridge",
            item_name="water",
            requested_quantity=3,
        )

        self.assertIsInstance(quote.source_name, str)
        self.assertTrue(quote.source_name.strip())

        self.assertIsInstance(quote.reason, str)
        self.assertTrue(quote.reason.strip())

    def test_contract_fulfillment_matches_availability(self):
        source = self.make_source()

        quote = source.quote_supply(
            location="North Ridge",
            item_name="water",
            requested_quantity=3,
        )

        expected_result = (
            quote.available_quantity
            >= quote.requested_quantity
        )

        self.assertEqual(
            quote.can_fulfill,
            expected_result,
        )


class TestSettlementWarehouseContract(
    SupplySourceContractTests,
    unittest.TestCase,
):
    """
    Run the shared contract against SettlementWarehouse.
    """

    def make_source(self):
        return SettlementWarehouse(
            name="Dry Creek Warehouse",
            inventory={"water": 10},
        )


class TestTradingPostContract(
    SupplySourceContractTests,
    unittest.TestCase,
):
    """
    Run the shared contract against TradingPost.
    """

    def make_source(self):
        return TradingPost(
            name="Morrow Trading Post",
            inventory={"water": 10},
            reserve_quantity=4,
        )


# ============================================================
# CONTRACT AND SWAP TESTS
# ============================================================


class TestContractAndSwap(unittest.TestCase):
    """
    Tests for the explicit contract and meaningful substitution.
    """

    def test_abstract_contract_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            SupplySource()

    def test_both_objects_satisfy_the_explicit_abc_contract(self):
        warehouse = SettlementWarehouse(
            name="Dry Creek Warehouse",
            inventory={"water": 10},
        )

        trading_post = TradingPost(
            name="Morrow Trading Post",
            inventory={"water": 10},
            reserve_quantity=5,
        )

        self.assertIsInstance(
            warehouse,
            SupplySource,
        )

        self.assertIsInstance(
            trading_post,
            SupplySource,
        )

    def test_same_caller_can_swap_between_two_supply_sources(self):
        """
        This is the focused contract-and-swap test.

        The caller performs the same operation with each collaborator.
        Only the supplied object changes.
        """

        sources = [
            SettlementWarehouse(
                name="Dry Creek Warehouse",
                inventory={"water": 10},
            ),
            TradingPost(
                name="Morrow Trading Post",
                inventory={"water": 10},
                reserve_quantity=5,
            ),
        ]

        decisions = []

        for source in sources:
            with self.subTest(
                source_type=type(source).__name__
            ):
                planner = ExpeditionPlanner(source)

                decision = planner.evaluate_supply_request(
                    location="North Ridge",
                    item_name="water",
                    requested_quantity=7,
                )

                self.assertIsInstance(
                    decision,
                    SupplyDecision,
                )
                self.assertEqual(
                    decision.location,
                    "North Ridge",
                )
                self.assertEqual(
                    decision.item_name,
                    "water",
                )
                self.assertEqual(
                    decision.requested_quantity,
                    7,
                )

                decisions.append(decision)

        self.assertTrue(decisions[0].approved)
        self.assertFalse(decisions[1].approved)

        self.assertNotEqual(
            decisions[0].source_name,
            decisions[1].source_name,
        )

    def test_protocol_allows_a_structural_test_double(self):
        """
        The test double fulfills the structural promise without inheriting
        from SupplySource.
        """

        class FixedSupplySource:
            def quote_supply(
                self,
                location,
                item_name,
                requested_quantity,
            ):
                return SupplyQuote(
                    source_name="Test Supply Source",
                    item_name=item_name,
                    requested_quantity=requested_quantity,
                    available_quantity=requested_quantity,
                    can_fulfill=True,
                    reason="The test source has enough supply.",
                )

        source = FixedSupplySource()
        planner = ExpeditionPlanner(source)

        decision = planner.evaluate_supply_request(
            location="North Ridge",
            item_name="water",
            requested_quantity=2,
        )

        self.assertIsInstance(
            source,
            SupplySourceProtocol,
        )
        self.assertTrue(decision.approved)


# ============================================================
# COLLABORATOR-SPECIFIC TESTS
# ============================================================


class TestSettlementWarehouseBehavior(unittest.TestCase):
    """
    Tests that belong specifically to SettlementWarehouse.
    """

    def test_warehouse_remembers_quoted_locations(self):
        warehouse = SettlementWarehouse(
            name="Dry Creek Warehouse",
            inventory={"water": 10},
        )

        warehouse.quote_supply(
            "North Ridge",
            "water",
            2,
        )
        warehouse.quote_supply(
            "Canyon Pass",
            "water",
            2,
        )

        self.assertEqual(
            warehouse.quoted_locations,
            frozenset(
                {
                    "North Ridge",
                    "Canyon Pass",
                }
            ),
        )

    def test_issuing_supply_changes_future_availability(self):
        warehouse = SettlementWarehouse(
            name="Dry Creek Warehouse",
            inventory={"water": 10},
        )

        warehouse.issue_supply(
            location="North Ridge",
            item_name="water",
            quantity=6,
        )

        later_quote = warehouse.quote_supply(
            location="Canyon Pass",
            item_name="water",
            requested_quantity=5,
        )

        self.assertEqual(
            warehouse.quantity_on_hand("water"),
            4,
        )
        self.assertEqual(
            later_quote.available_quantity,
            4,
        )
        self.assertFalse(
            later_quote.can_fulfill
        )

    def test_warehouse_records_completed_issues(self):
        warehouse = SettlementWarehouse(
            name="Dry Creek Warehouse",
            inventory={"water": 10},
        )

        warehouse.issue_supply(
            location="North Ridge",
            item_name="water",
            quantity=3,
        )

        self.assertEqual(
            warehouse.completed_issues,
            (
                (
                    "North Ridge",
                    "water",
                    3,
                ),
            ),
        )


class TestTradingPostBehavior(unittest.TestCase):
    """
    Tests that belong specifically to TradingPost.
    """

    def test_trading_post_protects_its_local_reserve(self):
        trading_post = TradingPost(
            name="Morrow Trading Post",
            inventory={"water": 10},
            reserve_quantity=4,
        )

        quote = trading_post.quote_supply(
            location="North Ridge",
            item_name="water",
            requested_quantity=7,
        )

        self.assertEqual(
            trading_post.quantity_on_hand("water"),
            10,
        )
        self.assertEqual(
            trading_post.quantity_available_for_trade("water"),
            6,
        )
        self.assertEqual(
            quote.available_quantity,
            6,
        )
        self.assertFalse(
            quote.can_fulfill
        )

    def test_trading_post_tracks_quote_activity(self):
        trading_post = TradingPost(
            name="Morrow Trading Post",
            inventory={"water": 10},
            reserve_quantity=4,
        )

        trading_post.quote_supply(
            "North Ridge",
            "water",
            2,
        )
        trading_post.quote_supply(
            "Canyon Pass",
            "water",
            2,
        )

        self.assertEqual(
            trading_post.quote_count,
            2,
        )
        self.assertEqual(
            trading_post.locations_served,
            frozenset(
                {
                    "North Ridge",
                    "Canyon Pass",
                }
            ),
        )


# ============================================================
# CALLER-BOUNDARY TESTS
# ============================================================


class TestCallerBoundary(unittest.TestCase):
    """
    Tests for input validation, contract enforcement, and failure handling.
    """

    def setUp(self):
        self.warehouse = SettlementWarehouse(
            name="Dry Creek Warehouse",
            inventory={"water": 10},
        )

        self.planner = ExpeditionPlanner(
            self.warehouse
        )

    def test_caller_rejects_empty_location(self):
        with self.assertRaises(ValueError):
            self.planner.evaluate_supply_request(
                location="   ",
                item_name="water",
                requested_quantity=2,
            )

    def test_caller_rejects_non_string_location(self):
        with self.assertRaises(TypeError):
            self.planner.evaluate_supply_request(
                location=42,
                item_name="water",
                requested_quantity=2,
            )

    def test_caller_rejects_empty_item_name(self):
        with self.assertRaises(ValueError):
            self.planner.evaluate_supply_request(
                location="North Ridge",
                item_name="",
                requested_quantity=2,
            )

    def test_caller_rejects_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.planner.evaluate_supply_request(
                location="North Ridge",
                item_name="water",
                requested_quantity=0,
            )

    def test_caller_rejects_non_integer_quantity(self):
        with self.assertRaises(TypeError):
            self.planner.evaluate_supply_request(
                location="North Ridge",
                item_name="water",
                requested_quantity=2.5,
            )

    def test_caller_rejects_boolean_quantity(self):
        with self.assertRaises(TypeError):
            self.planner.evaluate_supply_request(
                location="North Ridge",
                item_name="water",
                requested_quantity=True,
            )

    def test_caller_creates_and_remembers_a_decision(self):
        decision = self.planner.evaluate_supply_request(
            location="North Ridge",
            item_name="water",
            requested_quantity=3,
        )

        self.assertTrue(decision.approved)
        self.assertEqual(
            decision.approved_quantity,
            3,
        )
        self.assertIs(
            self.planner.last_decision,
            decision,
        )
        self.assertEqual(
            self.planner.decision_history,
            (decision,),
        )

    def test_caller_adds_context_when_collaborator_fails(self):
        class CrashingSupplySource:
            def quote_supply(
                self,
                location,
                item_name,
                requested_quantity,
            ):
                raise RuntimeError(
                    "telegraph line is down"
                )

        planner = ExpeditionPlanner(
            CrashingSupplySource()
        )

        with self.assertRaises(
            SupplySourceError
        ) as caught:
            planner.evaluate_supply_request(
                location="North Ridge",
                item_name="water",
                requested_quantity=3,
            )

        self.assertIn(
            "North Ridge",
            str(caught.exception),
        )
        self.assertIn(
            "telegraph line is down",
            str(caught.exception),
        )

    def test_caller_rejects_wrong_return_type(self):
        class BadSupplySource:
            def quote_supply(
                self,
                location,
                item_name,
                requested_quantity,
            ):
                return None

        planner = ExpeditionPlanner(
            BadSupplySource()
        )

        with self.assertRaises(
            ContractViolationError
        ) as caught:
            planner.evaluate_supply_request(
                location="North Ridge",
                item_name="water",
                requested_quantity=3,
            )

        self.assertIn(
            "SupplyQuote",
            str(caught.exception),
        )
        self.assertIn(
            "NoneType",
            str(caught.exception),
        )

    def test_caller_rejects_quote_for_wrong_item(self):
        class ConfusedSupplySource:
            def quote_supply(
                self,
                location,
                item_name,
                requested_quantity,
            ):
                return SupplyQuote(
                    source_name="Confused Source",
                    item_name="beans",
                    requested_quantity=requested_quantity,
                    available_quantity=10,
                    can_fulfill=True,
                    reason="The source quoted the wrong item.",
                )

        planner = ExpeditionPlanner(
            ConfusedSupplySource()
        )

        with self.assertRaises(
            ContractViolationError
        ):
            planner.evaluate_supply_request(
                location="North Ridge",
                item_name="water",
                requested_quantity=3,
            )

    def test_caller_rejects_contradictory_quote(self):
        class DishonestSupplySource:
            def quote_supply(
                self,
                location,
                item_name,
                requested_quantity,
            ):
                return SupplyQuote(
                    source_name="Dishonest Source",
                    item_name=item_name,
                    requested_quantity=requested_quantity,
                    available_quantity=1,
                    can_fulfill=True,
                    reason="The source claims it has enough.",
                )

        planner = ExpeditionPlanner(
            DishonestSupplySource()
        )

        with self.assertRaises(
            ContractViolationError
        ):
            planner.evaluate_supply_request(
                location="North Ridge",
                item_name="water",
                requested_quantity=3,
            )

    def test_constructor_rejects_object_without_required_operation(self):
        class NotASupplySource:
            pass

        with self.assertRaises(TypeError):
            ExpeditionPlanner(
                NotASupplySource()
            )


# ============================================================
# WORKING DEMONSTRATION
# ============================================================


def display_decision(decision: SupplyDecision) -> None:
    """
    Print one decision without placing display responsibilities in the
    domain objects.
    """

    status = (
        "APPROVED"
        if decision.approved
        else "DECLINED"
    )

    print(f"Decision: {status}")
    print(f"Location: {decision.location}")
    print(f"Item: {decision.item_name}")
    print(
        f"Requested quantity: "
        f"{decision.requested_quantity}"
    )
    print(
        f"Approved quantity: "
        f"{decision.approved_quantity}"
    )
    print(f"Source: {decision.source_name}")
    print(f"Explanation: {decision.explanation}")


def run_demonstration() -> None:
    """
    Demonstrate the contract and swap with visible output.
    """

    print()
    print("FRONTIER SETTLEMENT SUPPLY PLANNER")
    print("=" * 56)

    warehouse = SettlementWarehouse(
        name="Dry Creek Warehouse",
        inventory={
            "water": 10,
            "beans": 20,
        },
    )

    trading_post = TradingPost(
        name="Morrow Trading Post",
        inventory={
            "water": 10,
            "beans": 20,
        },
        reserve_quantity=5,
    )

    print()
    print("FIRST COLLABORATOR: SETTLEMENT WAREHOUSE")
    print("-" * 56)

    warehouse_planner = ExpeditionPlanner(
        warehouse
    )

    warehouse_decision = (
        warehouse_planner.evaluate_supply_request(
            location="North Ridge",
            item_name="water",
            requested_quantity=7,
        )
    )

    display_decision(
        warehouse_decision
    )

    print()
    print("Warehouse state after the quote:")
    print(
        "Quoted locations: "
        f"{sorted(warehouse.quoted_locations)}"
    )
    print(
        "Water on hand: "
        f"{warehouse.quantity_on_hand('water')}"
    )

    print()
    print("SWAPPED COLLABORATOR: TRADING POST")
    print("-" * 56)

    trading_post_planner = ExpeditionPlanner(
        trading_post
    )

    trading_post_decision = (
        trading_post_planner.evaluate_supply_request(
            location="North Ridge",
            item_name="water",
            requested_quantity=7,
        )
    )

    display_decision(
        trading_post_decision
    )

    print()
    print("Trading-post state after the quote:")
    print(
        f"Quote count: {trading_post.quote_count}"
    )
    print(
        "Locations served: "
        f"{sorted(trading_post.locations_served)}"
    )
    print(
        "Water available for trade: "
        f"{trading_post.quantity_available_for_trade('water')}"
    )

    print()
    print("WHAT THE SWAP PROVED")
    print("-" * 56)
    print(
        "The same caller sent the same request through "
        "the same contract."
    )
    print(
        "The warehouse approved the request because all "
        "10 units were available."
    )
    print(
        "The trading post declined the request because "
        "5 units were protected."
    )
    print(
        "The caller required no warehouse-specific or "
        "trading-post-specific branch."
    )


# ============================================================
# CONCISE WORLD BIBLE ENTRY
# ============================================================


WORLD_BIBLE_ENTRY = """
WORLD BIBLE: WEEK 7 CONTRACT AND SWAP
====================================

1. WORLD PREMISE

Dry Creek is a frontier settlement that sends expeditions to nearby
locations. Expeditions need supplies, but different supply sources follow
different rules about what they are willing to provide.

2. CAST

- Expedition planner
- Settlement warehouse
- Trading post
- Supply source
- Supply quote
- Supply decision
- Location
- Inventory

3. ONE REAL FLOW

An expedition requests supplies. The planner validates the request and asks
its current supply source for a quote. The source examines its own state and
returns a structured SupplyQuote. The planner verifies the quote, approves or
declines the request, and records the resulting decision.

4. THREE SOFTWARE QUESTIONS

- Can the selected source fulfill the request?
- How much stock is the source willing to provide?
- Why was the request approved or declined?

5. KNOWN UNKNOWNS

- Should approval automatically remove inventory?
- Should a quote expire when inventory changes?
- Can several sources combine partial supplies?

6. OBJECT PREDICTIONS

SettlementWarehouse deserves an object boundary because it owns inventory,
quoted locations, completed issues, and the rules for changing stock.

TradingPost deserves an object boundary because it owns inventory, a local
reserve, quote history, and different availability rules.

ExpeditionPlanner deserves an object boundary because it validates requests,
handles failures, enforces the collaborator contract, makes decisions, and
records decision history.

WEEK 7 CHANGE

The planner's dependency became the explicit SupplySource contract.
SettlementWarehouse and TradingPost are two stateful, swappable
implementations.

EVIDENCE

Reusable unittest contract tests run against both implementations. A focused
swap test sends the same request through the same caller. The warehouse
approves seven units, while the trading post declines because it protects a
reserve.

CALLER BOUNDARY

ExpeditionPlanner.evaluate_supply_request() is the caller boundary. It
validates input, calls the collaborator, handles failure, checks the returned
SupplyQuote, creates a SupplyDecision, and records the result.

REMAINING DEBT

Approval does not yet remove supplies from inventory. A future design should
separate quoting from committing supplies, perhaps with a reservation object.
"""


def display_world_bible() -> None:
    """
    Display the World Bible entry.
    """

    print()
    print(WORLD_BIBLE_ENTRY.strip())


# ============================================================
# TEST RUNNER AND PROGRAM ENTRY POINT
# ============================================================


def run_tests() -> unittest.result.TestResult:
    """
    Load and run every unittest in this file.
    """

    suite = unittest.defaultTestLoader.loadTestsFromModule(
        sys.modules[__name__]
    )

    runner = unittest.TextTestRunner(
        verbosity=2
    )

    return runner.run(suite)


def print_usage() -> None:
    """
    Show the available commands.
    """

    print(
        "Usage: python class_example.py "
        "[all|test|demo|bible]"
    )


def main() -> None:
    """
    Run tests, demonstration, and reflection from one Python file.
    """

    command = (
        sys.argv[1].lower()
        if len(sys.argv) > 1
        else "all"
    )

    valid_commands = {
        "all",
        "test",
        "tests",
        "demo",
        "bible",
    }

    if command not in valid_commands:
        print_usage()
        raise SystemExit(2)

    if command in {"all", "test", "tests"}:
        test_result = run_tests()

        if not test_result.wasSuccessful():
            raise SystemExit(1)

    if command == "all":
        run_demonstration()
        display_world_bible()

    elif command == "demo":
        run_demonstration()

    elif command == "bible":
        display_world_bible()


if __name__ == "__main__":
    main()