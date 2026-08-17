"""Shared strategy contract that keeps CS1 functions and CS2 objects compatible."""

from abc import ABC, abstractmethod

VALID_ACTIONS = {"roll", "bank"}


class Strategy(ABC):
    """A swappable Farkle decision collaborator."""

    name = "strategy"
    complexity_note = "unspecified"

    @abstractmethod
    def decide(self, state):
        """Return ``roll`` or ``bank`` for one public decision state."""

    def __call__(self, state):
        action = self.decide(state)
        if action not in VALID_ACTIONS:
            raise ValueError(
                f"{self.name} returned {action!r}; expected 'roll' or 'bank'"
            )
        return action


class FunctionStrategyAdapter(Strategy):
    """Adapt a plain function strategy without rewriting it."""

    def __init__(self, function, name=None, complexity_note="single rule/function"):
        self.function = function
        self.name = name or getattr(function, "__name__", "function_strategy")
        self.complexity_note = complexity_note

    def decide(self, state):
        return self.function(state)


class ValidatingStrategy(Strategy):
    """Composition wrapper that validates any callable at the contract edge."""

    def __init__(self, wrapped, name=None):
        self.wrapped = wrapped
        self.name = name or getattr(
            wrapped, "name", getattr(wrapped, "__name__", "strategy")
        )
        self.complexity_note = getattr(
            wrapped, "complexity_note", "wrapped callable"
        )

    def decide(self, state):
        return self.wrapped(state)
