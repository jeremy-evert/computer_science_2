# Future Improvements

## Reserve and issue approved supplies

The current example intentionally treats a supply decision as a quote: a full
or partial approval records what a source can provide, but does not reduce its
inventory.

A future version should separate these stages:

1. Request a quote.
2. Approve all or part of the request.
3. Create a reservation for the approved quantity.
4. Issue the reserved supply and reduce inventory.

This would prevent two approved requests from relying on the same stock and
would give reservations a clear expiration or cancellation rule. It is kept
out of the current lesson so the focus remains on the shared contract and
swappable collaborators.
