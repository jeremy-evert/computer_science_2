# Week 9 micro-lab — Compact Tkinter model, view, and event

## Goal

Keep a small domain model testable without a GUI, then let a modest Tkinter
view call that model through one meaningful callback. This is an
instructor-owned pattern, not a second homework project or a desktop-app
engineering unit.

```python
class CounterModel:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1
        return self.value

# Test without Tkinter: assert CounterModel().add() == 1
# A view callback calls model.add(), then refreshes a StringVar.
```

The view has an **Add** button. Its callback changes the model, refreshes
displayed state, and can be predicted before running. Students verify the
model with a direct test/trace, then bridge the pattern to a settlement
action, case update, ship command, or inventory operation. A second callback
such as Reset is welcome only if it improves the small experience; domain
rules do not belong only in callbacks.

## Tiny optional micro-practice menu

- Week 5: composition-versus-inheritance decision card.
- Week 6: two-object polymorphic-dispatch trace.
- Week 7: swap a fake collaborator against a contract test.
- Week 8: push/pop and enqueue/dequeue trace using a real world flow.
- Week 9: search/order trace and maintenance-cost discussion.
- Week 10: predict what the callback changes before running it.

These are in-class, pair, low-stakes, or optional supports. They are not a
parallel required problem-set sequence.
