"""Peer swap: python3 contract_test.py their_module   (default: inventory)
Passes if the model keeps the agreed method names and return values."""
import importlib
import sys

mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else "inventory")
cls = next(v for k, v in vars(mod).items() if isinstance(v, type) and hasattr(v, "restock"))
m = cls()
assert hasattr(m, "restock") and hasattr(m, "count"), "need restock and count"
assert isinstance(m.restock("x"), int), "restock must return an int"
assert m.count() == 1, "count must report 1 after one restock"
print("contract holds for", cls.__name__)
