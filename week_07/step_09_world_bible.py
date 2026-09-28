"""Step 9: the concise World Bible reflection for this example."""

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

