# Reasoning Odyssey Gate -- Week 7 -- Contract and Swap (S03/S08)

**Gate status:** active

**Grading:** 40 points; Reasoning Odyssey checkpoints (15% group);
**graded discussion** with a code/evidence attachment or repository link.

This checkpoint is a shared learning resource. Your classmates will be able to
see your post and learn from the choices and evidence you share. Submit a
working, small extension of your own Weeks 4--6 world: the project, contract
test, explanation, demonstration, reflection, and World Bible entry.

This is not a weekly mini-project. Do not build a hierarchy, GUI, algorithm, or
second system just to satisfy the gate.

## Required evidence

Pause and look back across Weeks 4--6: what does your growing system actually
depend on right now? Pick one real dependency and turn its promise into an
explicit contract.

Your discussion post must include:

1. A repository link or code attachment containing an ABC with an abstract
   method, plus two stateful concrete collaborators that implement the same
   promise in genuinely different ways.
2. One focused unittest that uses the same caller operation and request with
   both collaborators. Assert the shared contract, not exact wording from one
   implementation.
3. A plain-language explanation of the caller boundary: input validation,
   delegation, returned-value checking, and how a collaborator failure gains
   useful context.
4. A short demonstration result and a concise World Bible update recording
   what changed, evidence used, and remaining debt.

The typing Protocol comparison is optional only, never the graded mechanism.

## Discussion participation

Reply constructively to at least two classmates. Point to a particular design
choice or test, ask a useful question, or describe an idea you can carry into
your own program. Keep feedback specific, respectful, and grounded in the
posted evidence. Do not post private or identifying information about yourself
or anyone else.

## Scoring

| Criterion | Points |
|---|---:|
| Real explicit contract and two distinct stateful collaborators | 15 |
| Focused contract-and-swap test | 10 |
| Caller-boundary reasoning | 10 |
| Demonstration and World Bible update | 5 |

For a guided example and a narrative walkthrough, see
week_07/00_start_here.md and week_07/week_07_guided_path.pdf.
