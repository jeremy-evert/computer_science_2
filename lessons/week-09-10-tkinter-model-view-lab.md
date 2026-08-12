# Week 9–10 micro-lab — Tkinter model, view, and events

## Goal

Keep a small domain model testable without a GUI, then let a Tkinter view
call that model through two callbacks. This is an instructor-owned pattern,
not a second homework project.

```python
class CounterModel:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value += 1
        return self.value

    def reset(self):
        self.value = 0
        return self.value

# Test without Tkinter: assert CounterModel().add() == 1
# View callbacks call model.add()/model.reset(), then refresh a StringVar.
```

The view has an **Add** button and a **Reset** button; each callback changes
the model, refreshes displayed state, and can be predicted before running.
Students verify the model with a direct test/trace, then bridge the pattern
to a settlement action, case update, ship command, or inventory operation.
The GUI must stay modest and accessible; do not place domain rules only in
callbacks.

## Tiny optional micro-practice menu

- Week 4: composition-versus-inheritance decision card.
- Week 5: two-object polymorphic-dispatch trace.
- Week 6: swap a fake collaborator against a contract test.
- Week 7: push/pop and enqueue/dequeue trace using a real world flow.
- Week 8: search/order trace and maintenance-cost discussion.
- Week 10: predict callback state before running it.

These are in-class, pair, low-stakes, or optional supports. They are not a
parallel required problem-set sequence.
