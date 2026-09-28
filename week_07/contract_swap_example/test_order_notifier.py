import unittest

from order_notifier import (
    KitchenBell,
    OrderNotifier,
    TicketPrinter,
    announce_order_ready,
)


class TestOrderNotifier(unittest.TestCase):

    def test_kitchen_bell_announces_the_order(self):
        bell = KitchenBell()

        result = announce_order_ready(bell, "table 4 burger")

        self.assertEqual(
            result,
            "Ring! Order ready: table 4 burger"
        )

    def test_ticket_printer_announces_the_order(self):
        printer = TicketPrinter()

        result = announce_order_ready(printer, "table 4 burger")

        self.assertEqual(
            result,
            "Printed ticket: table 4 burger READY"
        )

    def test_announce_order_ready_holds_the_contract_for_either_collaborator(self):
        # The focused swap test: same caller, two different concrete
        # collaborators, one contract -- every notify() message must
        # actually name the order, regardless of which device answers it.
        order_name = "table 4 burger"
        notifiers = [KitchenBell(), TicketPrinter()]

        for notifier in notifiers:
            with self.subTest(notifier=type(notifier).__name__):
                result = announce_order_ready(notifier, order_name)
                self.assertIn(order_name, result)

    def test_announce_order_ready_accepts_a_notifier_it_has_never_seen(self):
        # Guards against a caller that secretly special-cases KitchenBell or
        # TicketPrinter: a brand-new conforming collaborator, written after
        # announce_order_ready, must still work without editing it.
        class Pager(OrderNotifier):
            def notify(self, order_name: str) -> str:
                return f"Buzz buzz: {order_name} is up"

        result = announce_order_ready(Pager(), "table 9 salad")

        self.assertIn("table 9 salad", result)

    def test_the_contract_is_enforced_not_just_documented(self):
        # What abc.ABC buys over a plain duck-typed class or
        # typing.Protocol: an incomplete collaborator cannot even be
        # constructed, so the contract can't be silently half-broken.
        class SilentSpeaker(OrderNotifier):
            pass

        with self.assertRaises(TypeError):
            SilentSpeaker()


if __name__ == "__main__":
    unittest.main(verbosity=2)
