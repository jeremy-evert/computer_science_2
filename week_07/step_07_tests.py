"""Step 7: contract, behavior, and caller-boundary tests."""

import unittest

from step_01_values import ContractViolationError, SupplyDecision, SupplyQuote, SupplySourceError
from step_02_contracts import SupplySource, SupplySourceProtocol
from step_04_warehouse import SettlementWarehouse
from step_05_trading_post import TradingPost
from step_06_planner import ExpeditionPlanner

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

