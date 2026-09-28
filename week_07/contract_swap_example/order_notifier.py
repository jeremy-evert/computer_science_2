from abc import ABC, abstractmethod


class OrderNotifier(ABC):
    """Contract: tell someone an order is ready. Every concrete notifier
    must return a message that actually names the order -- the caller
    below depends on that, not on which device answers it."""

    @abstractmethod
    def notify(self, order_name: str) -> str:
        raise NotImplementedError


class KitchenBell(OrderNotifier):

    def notify(self, order_name: str) -> str:
        return f"Ring! Order ready: {order_name}"


class TicketPrinter(OrderNotifier):

    def notify(self, order_name: str) -> str:
        return f"Printed ticket: {order_name} READY"


def announce_order_ready(notifier: OrderNotifier, order_name: str) -> str:
    return notifier.notify(order_name)
