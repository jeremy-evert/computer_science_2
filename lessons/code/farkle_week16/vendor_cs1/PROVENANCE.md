# Vendored CS1 Farkle provenance

This directory is **not** a second canonical Farkle rules implementation.

Canonical owner: `jeremy-evert/computer_science_1`  
Pinned source state for this CS2 build: `b546ca2f846ea0c788ad17e5667b8b471efb33fa`  
Core hardening code landed through: `828a6d07ec00740a4c5ccd2cbebdce778e579666`  
Date vendored: 2026-08-16

Vendored modules:

- `engine.py`
- `strategies.py`
- `learner.py`
- `simulate.py`

Why vendor instead of importing a sibling checkout:

- the CS2 Week 16 lab should run from a standalone CS2 checkout;
- the current course repository ecosystem has no shared package registry;
- a sibling-path import would be brittle for students;
- creating package infrastructure merely for Week 16 would violate scope.

## Drift rule

When CS1 changes the public Farkle contract, this snapshot must be deliberately reviewed and refreshed. Do not silently edit the game rules here.

The CS2 validation suite checks a small public-contract fingerprint: rule constants, state keys, dynamic threshold strategy support, balanced comparison starter accounting, and player-specific turn fields. It does not pretend to replace CS1's full engine tests.

If this same cross-repo vendoring problem appears a third time, promote the stable baseline into shared automation/package ownership rather than creating a third independent copy.
