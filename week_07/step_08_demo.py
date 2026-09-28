"""Step 8: a visible demonstration of swapping collaborators."""

from step_01_values import SupplyDecision
from step_04_warehouse import SettlementWarehouse
from step_05_trading_post import TradingPost
from step_06_planner import ExpeditionPlanner

def display_decision(decision: SupplyDecision) -> None:
    """
    Print one decision without placing display responsibilities in the
    domain objects.
    """

    status = decision.status.name

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
        "The trading post partially approved 5 units because "
        "5 units were protected."
    )
    print(
        "The caller required no warehouse-specific or "
        "trading-post-specific branch."
    )


# ============================================================
# CONCISE WORLD BIBLE ENTRY
# ============================================================
