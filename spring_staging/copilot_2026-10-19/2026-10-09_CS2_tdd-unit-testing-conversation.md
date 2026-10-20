| Conversation topic | Test-driven development, unit tests, and earned substitution using Oven and Grill |
|--------------------|-----------------------------------------------------------------------------------|
| Date               | October 9, 2026                                                                   |
| Course             | CS2                                                                               |

# Summary

This conversation develops a small Python unittest example one Red-Green step at a time. It begins with a missing Oven implementation, adds a Grill with meaningfully different behavior, tests appliance capabilities, uses Git diffs as evidence, and finally demonstrates substitution through prepare_meal(appliance, food) without prematurely inventing an inheritance hierarchy.

Privacy note: One student name appearing in the conversation was replaced with “\[student info removed\]” in both the user message and the corresponding Copilot reply. No grades, student submissions, or student email content were included.

Transcript fidelity note: The transcript below preserves the conversation available in this chat, including code, commands, lists, and terminal output. The generated-file citation in one earlier Copilot reply could not be reproduced as an active chat citation inside Word, so it is identified in brackets at that point rather than invented.

# Conversation Transcript

## **Jeremy:**

Reopen your Week 5 collaborating objects. Look across them (and the rest of your Week 3 cast) for a true is-a relationship.  
Where a true is-a relationship exists, demonstrate two subtypes receiving one shared operation with meaningfully different behavior; otherwise document why composition is the better design. Do not invent a hierarchy.  
Continue the testing habit from Weeks 3-4: a small automated test that exercises the shared operation on each subtype is the clearest way to prove the behavior differs. A log line is welcome again here if useful -- optional.  
Keep one concise World Bible entry: what changed, evidence used, and any remaining debt.  
Rubric (25 points)  
CriterionPointsMeets expectation  
World fit/build  
8  
The bounded change is meaningful for the selected world; no artificial hierarchy is rewarded.  
Behavior/decision evidence  
7  
A test, trace, run, diff, or review receipt supports the claimed behavior.  
Trade-off reasoning / World Bible  
6  
Explains the substitution-or-composition decision in plain language.  
AI accountability  
4  
When AI was used: proposal, diff, independent test, reasoning, accept/reject decision.  
Points  
25  
Submitting  
a text entry box or a file upload  
  
CS2 Week 06 -- Overview  
Reasoning Odyssey Gate — Week 6 — Earned Substitution (S02)  
What are we learning? Inheritance and polymorphism, earned rather than assumed — recognizing when two things in your world genuinely share an operation but behave differently (a real is-a relationship), versus when they just happen to look similar and should stay separate, composed objects instead.  
What am I building/changing? Reopen your Week 5 collaborating objects (and the rest of your Week 3 cast). Look for a true is-a relationship — a family of things that share one operation but behave meaningfully differently. Where one genuinely exists, demonstrate two subtypes receiving that one shared operation with meaningfully different behavior. Where it doesn't, document why composition (Week 5's has-a) is still the better design instead. Either answer is a full pass — do not invent a hierarchy just to have one.  
How does my world connect? Continue the unittest habit from Weeks 4-5: a small automated test that calls the shared operation on each subtype is the clearest way to prove the behavior actually differs. A log line at the point of substitution is welcome again if it helps show which subtype ran and why — optional, not required.  
What evidence do I keep? One concise World Bible entry: what changed, what evidence you used, and any remaining debt.  
Illustrative example (optional — not the required scenario)  
Any reasonable is-a-or-not decision in your own world is a full pass; you don't need this exact shape. One way to see the difference:  
A Guard and a Turret in a Frontier-Settlement-style world both need to respond_to_intruder() — but a Guard walks toward the threat and a Turret rotates and fires. That's a genuine is-a: both really are "things that respond to intruders," just differently. Two subtypes, one shared operation, meaningfully different behavior — write one test that calls respond_to_intruder() on each and asserts the different outcome.  
Contrast that with last week's Vault: a Vault and a Keyholder are not two kinds of the same thing — a Vault doesn't respond to intruders the way a Keyholder does, they collaborate on a shared invariant instead. That's why Week 5 stayed composition. The test for you this week: pick a candidate pair from your own world and ask honestly which shape it actually is, not which one is more exciting to build.  
Success criteria (25 points)  
CriterionPointsMeets expectation  
Genuine substitution or composition decision  
8  
The bounded change is meaningful for the selected world; no artificial hierarchy is rewarded.  
Behavior / decision evidence  
7  
A test, trace, run, diff, or review receipt supports the claimed behavior.  
Trade-off reasoning / World Bible  
6  
Explains the substitution-or-composition decision in plain language.  
AI accountability  
4  
When AI was used: proposal, diff, independent test, reasoning, accept/reject decision.  
What exactly do I turn in? The Week 6 gate assignment — your subtype-or-composition code (or a link), your test, and your one-line World Bible entry.  
What carries forward? Week 7 is your first checkpoint (40 points) — it pauses and looks back across Weeks 4-6 at what your world's growing system actually depends on, and turns one real dependency into an explicit contract.  
  
We want to explore unit testing. and we want to have some unit testing examples. So where can we start and can you introduce test driven development?

## **Copilot:**

You can introduce \*\*test-driven development, or TDD\*\*, as a disciplined way to make the Week 6 design decision observable: first describe the behavior with a failing test, then write only enough code to pass, and finally improve the design without breaking the test.  
  
\## 1. The basic TDD loop  
  
TDD uses a short cycle:  
  
1. \*\*Red:\*\* Write a small test describing behavior that does not exist yet. Run it and observe the expected failure.  
2. \*\*Green:\*\* Write the smallest reasonable implementation that makes the test pass.  
3. \*\*Refactor:\*\* Improve names, remove duplication, or strengthen the design while keeping all tests passing.  
  
The important idea is:  
  
\> \*\*The test states what the world should do before the implementation decides how it will do it.\*\*  
  
For Week 6, the test should not merely prove that two classes exist. It should prove that:  
  
- both objects receive the \*\*same operation\*\*,  
- each object can be substituted into the same calling code,  
- each subtype produces \*\*meaningfully different behavior\*\*.  
  
\# 2. A Week 6 testing question  
  
Before writing inheritance, students can ask:  
  
\> Can one piece of calling code use either candidate object through the same operation without asking which specific type it received?  
  
For example, suppose a cooking world already contains an \`Oven\` and a \`Grill\`.  
  
Both can reasonably be described as a \*\*cooking appliance\*\*. Both can receive:

cook(food)

But their behavior differs:  
  
- an oven bakes the food with enclosed heat,  
- a grill cooks the food over direct heat.  
  
That is a plausible candidate for substitution. The hierarchy is justified by the world, not added merely to demonstrate inheritance.  
  
\# 3. One complete runnable example  
  
Save this as:

week06_tdd_cooking.py

Then run:

python .\week06_tdd_cooking.py

from abc import ABC, abstractmethod  
import unittest  
  
  
\# ============================================================  
\# IMPLEMENTATION  
\# ============================================================  
  
class CookingAppliance(ABC):  
"""  
Shared contract for something that can cook food.  
  
This parent class does not decide exactly how cooking works.  
Each subtype must provide its own cook() behavior.  
"""  
  
@abstractmethod  
def cook(self, food):  
pass  
  
  
class Oven(CookingAppliance):  
  
def cook(self, food):  
return f"The oven bakes the {food} with enclosed heat."  
  
  
class Grill(CookingAppliance):  
  
def cook(self, food):  
return f"The grill sears the {food} over direct heat."  
  
  
def prepare_meal(appliance, food):  
"""  
This function demonstrates substitution.  
  
It does not ask whether the appliance is an Oven or a Grill.  
It simply sends the shared cook() operation.  
"""  
print(f"LOG: Using {type(appliance).\_\_name\_\_} to prepare {food}.")  
return appliance.cook(food)  
  
  
\# ============================================================  
\# AUTOMATED TESTS  
\# ============================================================  
  
class TestCookingAppliances(unittest.TestCase):  
  
def test_oven_and_grill_respond_to_same_operation(self):  
appliances = \[  
Oven(),  
Grill(),  
\]  
  
results = \[  
prepare_meal(appliance, "vegetables")  
for appliance in appliances  
\]  
  
self.assertEqual(  
results\[0\],  
"The oven bakes the vegetables with enclosed heat."  
)  
  
self.assertEqual(  
results\[1\],  
"The grill sears the vegetables over direct heat."  
)  
  
def test_shared_operation_produces_different_behavior(self):  
oven_result = prepare_meal(Oven(), "potatoes")  
grill_result = prepare_meal(Grill(), "potatoes")  
  
self.assertNotEqual(oven_result, grill_result)  
self.assertIn("bakes", oven_result)  
self.assertIn("sears", grill_result)  
  
def test_each_subtype_can_be_substituted_into_prepare_meal(self):  
for appliance in \[Oven(), Grill()\]:  
with self.subTest(appliance=type(appliance).\_\_name\_\_):  
result = prepare_meal(appliance, "corn")  
  
self.assertIsInstance(result, str)  
self.assertIn("corn", result)  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)

A successful run should report three passing tests. The exact timing values can vary.  
  
\# 4. What each test proves  
  
\## Test 1: One shared operation

prepare_meal(appliance, "vegetables")

The same function works with an \`Oven\` or a \`Grill\`. It does not contain logic like:

if isinstance(appliance, Oven):

That absence is important. The calling code trusts the shared \`cook()\` contract.  
  
\## Test 2: Meaningfully different behavior

self.assertNotEqual(oven_result, grill_result)

This prevents a shallow example where both subtypes technically override a method but do essentially the same thing.  
  
The more specific assertions provide stronger evidence:

self.assertIn("bakes", oven_result)  
self.assertIn("sears", grill_result)

\## Test 3: Substitution

for appliance in \[Oven(), Grill()\]:

Each subtype is passed through the same calling path. This is the practical meaning of polymorphism in this example.  
  
\# 5. How to demonstrate actual TDD in class  
  
The completed file contains both implementation and tests, but the development history should proceed in smaller steps.  
  
\## Red: write the desired test first  
  
The student begins with a test similar to:

def test_oven_cooks_with_enclosed_heat(self):  
result = prepare_meal(Oven(), "bread")  
  
self.assertEqual(  
result,  
"The oven bakes the bread with enclosed heat."  
)

Run it before creating \`Oven\` or \`prepare_meal\`.  
  
The resulting error is useful evidence. It proves the test can detect that the feature is missing.  
  
\## Green: write the smallest implementation  
  
Add only enough code to make that test pass:

class Oven:  
  
def cook(self, food):  
return f"The oven bakes the {food} with enclosed heat."  
  
  
def prepare_meal(appliance, food):  
return appliance.cook(food)

Run the test again and observe the pass.  
  
\## Red again: require the second subtype  
  
Add a test for \`Grill\`:

def test_grill_cooks_with_direct_heat(self):  
result = prepare_meal(Grill(), "bread")  
  
self.assertEqual(  
result,  
"The grill sears the bread over direct heat."  
)

It fails because \`Grill\` does not exist.  
  
\## Green again  
  
Create \`Grill\` with its different behavior.  
  
\## Refactor  
  
Once both behaviors pass, introduce the explicit \`CookingAppliance\` contract if it makes the design clearer. Run the tests after the refactor to prove that behavior was preserved.  
  
\# 6. What if there is no honest is-a relationship?  
  
That is also a successful Week 6 result.  
  
Suppose the world contains:  
  
- a \`Recipe\`,  
- an \`Oven\`.  
  
An oven \*\*has a recipe available to guide its use\*\*, or a cook uses both objects together. But an oven is not a kind of recipe, and a recipe is not a kind of oven.  
  
Do not force this:

class Recipe(Oven):  
pass

Instead, retain composition:

class Recipe:  
  
def \_\_init\_\_(self, name, cooking_method):  
self.name = name  
self.cooking_method = cooking_method  
  
  
class Kitchen:  
  
def \_\_init\_\_(self, appliance):  
self.appliance = appliance  
  
def prepare(self, recipe):  
return self.appliance.cook(recipe.name)

The corresponding test would demonstrate collaboration, not substitution:

def test_kitchen_uses_its_appliance_to_prepare_recipe(self):  
kitchen = Kitchen(Oven())  
recipe = Recipe("bread", "bake")  
  
result = kitchen.prepare(recipe)  
  
self.assertIn("bread", result)  
self.assertIn("bakes", result)

Plain-language reasoning:  
  
\> A recipe and an oven collaborate, but they cannot replace one another. They have different responsibilities, so composition is the more honest design.  
  
\# 7. A student-friendly starting checklist  
  
Students can begin Week 6 with this process:  
  
1. List two existing objects from Weeks 3 through 5.  
2. Write the sentence: “A \_\_\_ is a kind of \_\_\_.”  
3. Decide whether that sentence remains true throughout the world.  
4. Identify one operation both candidates genuinely share.  
5. Describe how their behavior should differ.  
6. Write a test that calls the same operation on both objects.  
7. Run the test and keep the failing receipt.  
8. Implement the smallest change.  
9. Run the test again and keep the passing receipt.  
10. Record the decision in the World Bible.  
  
A warning sign is needing to say:  
  
\> “They are both classes, so they should share a parent.”  
  
That is a programming similarity, not a world relationship.  
  
\# 8. Concise World Bible entry  
  
Here is a version matching the assignment:  
  
\> \*\*Week 6:\*\* Identified \`Oven\` and \`Grill\` as kinds of \`CookingAppliance\` because both accept \`cook(food)\` but bake and sear differently. Automated tests exercised both through \`prepare_meal()\` and verified distinct results. Remaining debt: replace descriptive strings with changes to the food’s cooked state.  
  
If composition was selected:  
  
\> \*\*Week 6:\*\* Kept \`Recipe\` and \`Oven\` as composed collaborators because neither can substitute for the other. An automated test verified that the kitchen delegates preparation to its appliance. Remaining debt: validate whether each recipe supports the selected appliance.  
  
\# 9. AI accountability receipt  
  
Students who use AI can submit a compact record like this:  
  
\> \*\*AI proposal:\*\* AI suggested treating \`Oven\` and \`Grill\` as \`CookingAppliance\` subtypes with a shared \`cook()\` operation.  
\> \*\*Diff reviewed:\*\* I checked that the change added one parent contract, two subtype implementations, and tests without changing unrelated world objects.  
\> \*\*Independent test:\*\* I ran \`python .\week06_tdd_cooking.py\` and verified that all tests passed.  
\> \*\*Reasoning:\*\* Both objects can honestly substitute for a cooking appliance, but their cooking methods differ meaningfully.  
\> \*\*Decision:\*\* Accepted the hierarchy. I would reject a hierarchy between \`Recipe\` and \`Oven\` because those objects collaborate but cannot replace one another.  
  
\## Main teaching improvement  
  
This approach makes inheritance the \*\*conclusion of a tested world-design decision\*\*, not the starting requirement. TDD gives students a concrete receipt: the test failed before the behavior existed, passed after implementation, and continued passing after the design was cleaned up.

## **Jeremy:**

PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> pwd  
  
Path  
----  
C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example  
  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> ls  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
  
give me the simplest example of a failing test that is red. I want to see one red test and I want to build this example one step of the TDD loop at a time.

## **Copilot:**

Perfect. We will do \*\*only the Red step\*\* now: create one test for behavior that does not exist yet, run it, and observe its expected failure.  
  
Copy and run this entire PowerShell block from your current empty folder:

@'  
import unittest  
  
from cooking_appliance import Oven  
  
  
class TestOven(unittest.TestCase):  
  
def test_oven_bakes_bread(self):  
oven = Oven()  
  
result = oven.cook("bread")  
  
self.assertEqual(  
result,  
"The oven bakes the bread."  
)  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)  
'@ \| Set-Content -Encoding UTF8 .\test_cooking_appliance.py  
  
python .\test_cooking_appliance.py

\## Expected result: RED  
  
You should see an error resembling:

ModuleNotFoundError: No module named 'cooking_appliance'

This is a \*\*good failure\*\*.  
  
The test expects:  
  
- a file named \`cooking_appliance.py\`  
- an \`Oven\` class  
- a \`cook("bread")\` operation  
- the result \`"The oven bakes the bread."\`  
  
None of that implementation exists yet, so the test correctly turns red.  
  
Do \*\*not\*\* create \`cooking_appliance.py\` yet. Keep this failure visible because it is our first TDD evidence receipt:  
  
\> \*\*RED:\*\* The automated test failed because the requested cooking behavior had not been implemented.  
  
Our next step will be \*\*Green\*\*: create the smallest possible \`cooking_appliance.py\` that makes this one test pass.

## **Jeremy:**

PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> code .\test_cooking_appliance.py  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
Traceback (most recent call last):  
File "C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\test_cooking_appliance.py", line 3, in \<module\>  
from cooking_appliance import Oven  
ModuleNotFoundError: No module named 'cooking_appliance'  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
this is good. One file at a time. Next step please.  
  
also, lets use code to edit the documents instead of herestrings

## **Copilot:**

Excellent. We have completed \*\*Red\*\*. Now we begin \*\*Green\*\*, one file at a time, using VS Code.  
  
\## Next step: create the missing implementation file  
  
Run:

code .\cooking_appliance.py

In VS Code, enter this smallest useful implementation:

class Oven:  
  
def cook(self, food):  
return f"The oven bakes the {food}."

Save the file. Then return to PowerShell and run the existing test again:

python .\test_cooking_appliance.py

\## Expected result: GREEN

test_oven_bakes_bread (\_\_main\_\_.TestOven.test_oven_bakes_bread) ... ok  
  
----------------------------------------------------------------------  
Ran 1 test  
  
OK

If you get that result, we have completed one full \*\*Red → Green\*\* movement:  
  
- \*\*Red:\*\* \`cooking_appliance\` did not exist.  
- \*\*Green:\*\* We added the smallest implementation needed to satisfy the existing test.  
- We have \*\*not refactored or added a second behavior yet\*\*. One step at a time.

## **Jeremy:**

PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> ls  
  
Directory: C:\Users\<you>\git\computer_science_2\week_06\unit\_  
testing_example  
  
Mode LastWriteTime Length Name  
---- ------------- ------ ----  
-a---- 9/23/2026 1:22 PM 86 cooking_appliance  
.py  
-a---- 9/23/2026 1:15 PM 347 test_cooking_appl  
iance.py  
  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
test_oven_bakes_bread (\_\_main\_\_.TestOven.test_oven_bakes_bread) ... ok  
  
----------------------------------------------------------------------  
Ran 1 test in 0.000s  
  
OK  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> code .\test_cooking_appliance.py  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
  
okay. now we want our next failing test. What would be an interesting failing test that helps us build towards has a vs is a for an example. Please go slowly

## **Copilot:**

Excellent. We will make \*\*one small change to the test file only\*\*. The next Red test will introduce a \`Grill\`, which may also \`cook(food)\` but should behave differently from an \`Oven\`.  
  
\## Why this helps with “is-a”  
  
We are testing this idea:  
  
- An \`Oven\` can cook food.  
- A \`Grill\` can cook food.  
- They receive the same operation: \`cook("bread")\`.  
- They produce meaningfully different results.  
  
We are \*\*not creating a parent class yet\*\*. First, we gather behavioral evidence.  
  
\## Add one failing test  
  
You already opened the test file with:

code .\test_cooking_appliance.py

Inside \`TestOven\`, add this method below the existing test:

def test_grill_sears_bread(self):  
grill = Grill()  
  
result = grill.cook("bread")  
  
self.assertEqual(  
result,  
"The grill sears the bread."  
)

Also change the import at the top from:

from cooking_appliance import Oven

to:

from cooking_appliance import Grill, Oven

Save the test file, then run:

python .\test_cooking_appliance.py

\## Expected Red result  
  
You should receive an error similar to:

ImportError: cannot import name 'Grill' from 'cooking_appliance'

That is exactly the Red result we want. The test is requesting a second object with the same general operation:

cook("bread")

But with different expected behavior:

The grill sears the bread.

Stop after running it. Do not create \`Grill\` yet. This Red test is our evidence that the new behavior does not exist.

## **Jeremy:**

import unittest  
  
from cooking_appliance import Oven  
  
  
class TestOven(unittest.TestCase):  
  
def test_oven_bakes_bread(self):  
oven = Oven()  
  
result = oven.cook("bread")  
  
self.assertEqual(  
result,  
"The oven bakes the bread."  
)  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)  
  
please give me a one for one drop in replacement for this so I dont' have to guess where to drop things in.

## **Copilot:**

Absolutely. Replace \*\*all contents\*\* of \`test_cooking_appliance.py\` with this:

import unittest  
  
from cooking_appliance import Grill, Oven  
  
  
class TestCookingAppliance(unittest.TestCase):  
  
def test_oven_bakes_bread(self):  
oven = Oven()  
  
result = oven.cook("bread")  
  
self.assertEqual(  
result,  
"The oven bakes the bread."  
)  
  
def test_grill_sears_bread(self):  
grill = Grill()  
  
result = grill.cook("bread")  
  
self.assertEqual(  
result,  
"The grill sears the bread."  
)  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)

Save it, then run:

python . est_cooking_appliance.py

You should now get a \*\*Red\*\* error similar to:

ImportError: cannot import name 'Grill' from 'cooking_appliance'

That is the desired failure. We changed only the test file, and the test is now asking for behavior that has not been implemented.

## **Jeremy:**

PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
Traceback (most recent call last):  
File "C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\test_cooking_appliance.py", line 3, in \<module\>  
from cooking_appliance import Grill, Oven  
ImportError: cannot import name 'Grill' from 'cooking_appliance' (C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\cooking_appliance.py)  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
okay. so that worked. now what?

## **Copilot:**

Good. We have our second \*\*Red\*\* result. Now we make the smallest implementation change necessary to turn it \*\*Green\*\*.  
  
\## Open the implementation file

code .\cooking_appliance.py

Replace the \*\*entire contents\*\* with:

class Oven:  
  
def cook(self, food):  
return f"The oven bakes the {food}."  
  
  
class Grill:  
  
def cook(self, food):  
return f"The grill sears the {food}."

Save the file, then run:

python . est_cooking_appliance.py

\## Expected Green result

test_grill_sears_bread ... ok  
test_oven_bakes_bread ... ok  
  
----------------------------------------------------------------------  
Ran 2 tests  
  
OK

\## What we have established  
  
Both objects now receive the same operation:

cook(food)

But they behave differently:  
  
- \`Oven\` \*\*bakes\*\*  
- \`Grill\` \*\*sears\*\*  
  
We still have \*\*not\*\* added inheritance. We are first proving that the shared behavior exists. That keeps us from prematurely inventing a hierarchy.

## **Jeremy:**

PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
test_grill_sears_bread (\_\_main\_\_.TestCookingAppliance.test_grill_sears_bread) ... ok  
test_oven_bakes_bread (\_\_main\_\_.TestCookingAppliance.test_oven_bakes_bread) ... ok  
  
----------------------------------------------------------------------  
Ran 2 tests in 0.000s  
  
OK  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
  
\[student info removed\] wants to know what we can cook with those apliances? and how do we add a test for that? let us continue to grind through the unit testing example.

## **Copilot:**

\[student info removed\] has the right question: our appliances can currently cook \*\*any string\*\*, even \`"socks"\`. Let’s add a shared operation named \`can_cook(food)\` so each appliance can eventually describe what it reasonably cooks.  
  
For this step, we change \*\*only the test file\*\* and deliberately create one new Red test.  
  
\## Replace the entire test file  
  
Open it:

code . est_cooking_appliance.py

Replace everything in \`test_cooking_appliance.py\` with:

import unittest  
  
from cooking_appliance import Grill, Oven  
  
  
class TestCookingAppliance(unittest.TestCase):  
  
def test_oven_bakes_bread(self):  
oven = Oven()  
  
result = oven.cook("bread")  
  
self.assertEqual(  
result,  
"The oven bakes the bread."  
)  
  
def test_grill_sears_bread(self):  
grill = Grill()  
  
result = grill.cook("bread")  
  
self.assertEqual(  
result,  
"The grill sears the bread."  
)  
  
def test_oven_can_cook_pizza(self):  
oven = Oven()  
  
result = oven.can_cook("pizza")  
  
self.assertTrue(result)  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)

Save the file, then run:

python . est_cooking_appliance.py

\## Expected Red result  
  
The original two tests should still pass, but the new test should produce an error resembling:

AttributeError: 'Oven' object has no attribute 'can_cook'

That is our desired Red test.  
  
It states a new world rule:  
  
\> An oven can tell us whether it can cook a particular food, and pizza should be supported.  
  
Stop with the failure. We are not implementing \`can_cook()\` yet. This is the next \*\*Red\*\* receipt in our TDD loop.

## **Jeremy:**

is there a way that we can do a diff on those two files and see what changed? from the last time to this time?  
  
import unittest  
from cooking_appliance import Grill, Oven  
class TestCookingAppliance(unittest.TestCase):  
def test_oven_bakes_bread(self):  
oven = Oven()  
result = oven.cook("bread")  
self.assertEqual(  
result,  
"The oven bakes the bread."  
)  
def test_grill_sears_bread(self):  
grill = Grill()  
result = grill.cook("bread")  
self.assertEqual(  
result,  
"The grill sears the bread."  
)  
def test_oven_can_cook_pizza(self):  
oven = Oven()  
result = oven.can_cook("pizza")  
self.assertTrue(result)  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)

## **Copilot:**

Yes. Since this is a Git repository, Git can show exactly what changed since the last commit.  
  
\## See the changes in the test file  
  
Run:

git diff -- . est_cooking_appliance.py

You should see something similar to:

\+ def test_oven_can_cook_pizza(self):  
+ oven = Oven()  
+  
+ result = oven.can_cook("pizza")  
+  
+ self.assertTrue(result)

Lines beginning with \`+\` were added. Lines beginning with \`-\` were removed.  
  
\## See changes in both Python files

git diff -- .\cooking_appliance.py . est_cooking_appliance.py

At this stage, only the test file should show a new change because we have not yet implemented \`can_cook()\`.  
  
\## Important: Git needs a saved checkpoint  
  
\`git diff\` compares your current files with the last committed version. First check:

git status

If these files have never been committed, establish a checkpoint:

git add .\cooking_appliance.py . est_cooking_appliance.py  
git commit -m "Add passing oven and grill cooking tests"

After that checkpoint, add the new pizza test and run:

git diff -- . est_cooking_appliance.py

That gives you a clean receipt showing only the new failing test.  
  
\## One warning about the pasted code  
  
The version in your message lost its Python indentation. Keep the indented version in VS Code because Python requires indentation for the class, methods, and method bodies.  
  
For our TDD evidence, we now have:  
  
1. \*\*Previous checkpoint:\*\* two passing tests.  
2. \*\*Diff:\*\* one new test for \`oven.can_cook("pizza")\`.  
3. \*\*Next run:\*\* the new test should fail because \`can_cook()\` does not exist.  
  
That diff is excellent AI-accountability evidence because it shows precisely what changed rather than merely claiming that a test was added.

## **Jeremy:**

PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> ls  
  
Directory: C:\Users\<you>\git\computer_science_2\week_06\unit\_  
testing_example  
  
Mode LastWriteTime Length Name  
---- ------------- ------ ----  
d----- 9/23/2026 1:32 PM \_\_pycache\_\_  
-a---- 9/23/2026 1:32 PM 180 cooking_appliance  
.py  
-a---- 9/23/2026 1:34 PM 700 test_cooking_appl  
iance.py  
  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
test_grill_sears_bread (\_\_main\_\_.TestCookingAppliance.test_grill_sears_bread) ... ok  
test_oven_bakes_bread (\_\_main\_\_.TestCookingAppliance.test_oven_bakes_bread) ... ok  
test_oven_can_cook_pizza (\_\_main\_\_.TestCookingAppliance.test_oven_can_cook_pizza) ... ERROR  
  
======================================================================  
ERROR: test_oven_can_cook_pizza (\_\_main\_\_.TestCookingAppliance.test_oven_can_cook_pizza)  
----------------------------------------------------------------------  
Traceback (most recent call last):  
File "C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\test_cooking_appliance.py", line 31, in test_oven_can_cook_pizza  
result = oven.can_cook("pizza")  
^^^^^^^^^^^^^  
AttributeError: 'Oven' object has no attribute 'can_cook'  
  
----------------------------------------------------------------------  
Ran 3 tests in 0.012s  
  
FAILED (errors=1)  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
now we have our failing test.  
  
how do we fix this?

## **Copilot:**

Exactly. We are at \*\*Red\*\*, and now we make the smallest change needed for \*\*Green\*\*. Change only \`cooking_appliance.py\`. Leave the test file alone.  
  
\## 1. Open the implementation file

code .\cooking_appliance.py

Replace the \*\*entire file\*\* with:

class Oven:  
  
def cook(self, food):  
return f"The oven bakes the {food}."  
  
def can_cook(self, food):  
return food == "pizza"  
  
  
class Grill:  
  
def cook(self, food):  
return f"The grill sears the {food}."

Save the file.  
  
\## 2. Run all three tests

python . est_cooking_appliance.py

You should now see:

test_grill_sears_bread ... ok  
test_oven_bakes_bread ... ok  
test_oven_can_cook_pizza ... ok  
  
----------------------------------------------------------------------  
Ran 3 tests  
  
OK

\## Why this is the smallest fix  
  
Our failing test asks only one question:

oven.can_cook("pizza")

It expects \`True\`, so the smallest honest implementation is:

def can_cook(self, food):  
return food == "pizza"

We are deliberately \*\*not\*\* adding lists of foods, grill support, inheritance, or validation yet. TDD says to add only enough behavior to satisfy the current test.  
  
At that point we have completed another cycle:  
  
- \*\*Red:\*\* \`Oven\` had no \`can_cook()\` method.  
- \*\*Green:\*\* \`Oven.can_cook("pizza")\` now returns \`True\`.  
- \*\*Next:\*\* we can write a test that forces the method to distinguish something the oven can cook from something it cannot.

## **Jeremy:**

PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
test_grill_sears_bread (\_\_main\_\_.TestCookingAppliance.test_grill_sears_bread) ... ok  
test_oven_bakes_bread (\_\_main\_\_.TestCookingAppliance.test_oven_bakes_bread) ... ok  
test_oven_can_cook_pizza (\_\_main\_\_.TestCookingAppliance.test_oven_can_cook_pizza) ... ok  
  
----------------------------------------------------------------------  
Ran 3 tests in 0.000s  
  
OK  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
okay. now I want to add 3 new tests for the grill that would show us three more features we would like for the grill.

## **Copilot:**

Yes. Let’s add \*\*three failing tests at once\*\*, but change only the test file. These tests will ask the \`Grill\` for three new features:  
  
1. It can cook burgers.  
2. It cannot cook cake.  
3. It can report its cooking method.  
  
\## Open the test file

code . est_cooking_appliance.py

Replace the \*\*entire contents\*\* with:

import unittest  
  
from cooking_appliance import Grill, Oven  
  
  
class TestCookingAppliance(unittest.TestCase):  
  
def test_oven_bakes_bread(self):  
oven = Oven()  
  
result = oven.cook("bread")  
  
self.assertEqual(  
result,  
"The oven bakes the bread."  
)  
  
def test_grill_sears_bread(self):  
grill = Grill()  
  
result = grill.cook("bread")  
  
self.assertEqual(  
result,  
"The grill sears the bread."  
)  
  
def test_oven_can_cook_pizza(self):  
oven = Oven()  
  
result = oven.can_cook("pizza")  
  
self.assertTrue(result)  
  
def test_grill_can_cook_burgers(self):  
grill = Grill()  
  
result = grill.can_cook("burgers")  
  
self.assertTrue(result)  
  
def test_grill_cannot_cook_cake(self):  
grill = Grill()  
  
result = grill.can_cook("cake")  
  
self.assertFalse(result)  
  
def test_grill_reports_direct_heat(self):  
grill = Grill()  
  
result = grill.cooking_method()  
  
self.assertEqual(  
result,  
"direct heat"  
)  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)

Save the file, then run:

python . est_cooking_appliance.py

\## Expected Red result  
  
The original three tests should pass. The three new tests should fail because \`Grill\` does not yet have:

can_cook()

or:

cooking_method()

You should see errors resembling:

AttributeError: 'Grill' object has no attribute 'can_cook'

and:

AttributeError: 'Grill' object has no attribute 'cooking_method'

\## What these tests teach  
  
These tests exercise three different assertion patterns:

self.assertTrue(result)  
self.assertFalse(result)  
self.assertEqual(result, "direct heat")

They also begin defining the grill’s responsibility without changing the implementation yet. This is our next \*\*Red\*\* receipt.

## **Jeremy:**

PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
test_grill_can_cook_burgers (\_\_main\_\_.TestCookingAppliance.test_grill_can_cook_burgers) ... ERROR  
test_grill_cannot_cook_cake (\_\_main\_\_.TestCookingAppliance.test_grill_cannot_cook_cake) ... ERROR  
test_grill_reports_direct_heat (\_\_main\_\_.TestCookingAppliance.test_grill_reports_direct_heat) ... ERROR  
test_grill_sears_bread (\_\_main\_\_.TestCookingAppliance.test_grill_sears_bread) ... ok  
test_oven_bakes_bread (\_\_main\_\_.TestCookingAppliance.test_oven_bakes_bread) ... ok  
test_oven_can_cook_pizza (\_\_main\_\_.TestCookingAppliance.test_oven_can_cook_pizza) ... ok  
  
======================================================================  
ERROR: test_grill_can_cook_burgers (\_\_main\_\_.TestCookingAppliance.test_grill_can_cook_burgers)  
----------------------------------------------------------------------  
Traceback (most recent call last):  
File "C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\test_cooking_appliance.py", line 38, in test_grill_can_cook_burgers  
result = grill.can_cook("burgers")  
^^^^^^^^^^^^^^  
AttributeError: 'Grill' object has no attribute 'can_cook'  
  
======================================================================  
ERROR: test_grill_cannot_cook_cake (\_\_main\_\_.TestCookingAppliance.test_grill_cannot_cook_cake)  
----------------------------------------------------------------------  
Traceback (most recent call last):  
File "C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\test_cooking_appliance.py", line 45, in test_grill_cannot_cook_cake  
result = grill.can_cook("cake")  
^^^^^^^^^^^^^^  
AttributeError: 'Grill' object has no attribute 'can_cook'  
  
======================================================================  
ERROR: test_grill_reports_direct_heat (\_\_main\_\_.TestCookingAppliance.test_grill_reports_direct_heat)  
----------------------------------------------------------------------  
Traceback (most recent call last):  
File "C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\test_cooking_appliance.py", line 52, in test_grill_reports_direct_heat  
result = grill.cooking_method()  
^^^^^^^^^^^^^^^^^^^^  
AttributeError: 'Grill' object has no attribute 'cooking_method'  
  
----------------------------------------------------------------------  
Ran 6 tests in 0.013s  
  
FAILED (errors=3)  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
  
now let us make one new feature at a time. add the last failing test first. show us what we need to add.

## **Copilot:**

Good. We will fix \*\*only the last failing test\*\*:

test_grill_reports_direct_heat

Leave \`test_cooking_appliance.py\` unchanged.  
  
\## Open the implementation

code .\cooking_appliance.py

Replace the entire file with:

class Oven:  
  
def cook(self, food):  
return f"The oven bakes the {food}."  
  
def can_cook(self, food):  
return food == "pizza"  
  
  
class Grill:  
  
def cook(self, food):  
return f"The grill sears the {food}."  
  
def cooking_method(self):  
return "direct heat"

Save the file, then run:

python . est_cooking_appliance.py

\## Expected result  
  
You should now have:  
  
- \*\*4 passing tests\*\*  
- \*\*2 failing tests\*\*  
  
The fixed test should say:

test_grill_reports_direct_heat ... ok

The remaining two should still fail because \`Grill\` does not yet have \`can_cook()\`:

test_grill_can_cook_burgers ... ERROR  
test_grill_cannot_cook_cake ... ERROR

That is exactly what we want. We made one feature Green while preserving the other two Red tests.  
  
\### TDD receipt  
  
- \*\*Test requirement:\*\* A grill reports \`"direct heat"\`.  
- \*\*Implementation added:\*\* \`Grill.cooking_method()\`.  
- \*\*Expected evidence:\*\* One additional passing test, with two failures remaining.

## **Jeremy:**

class Oven:  
  
def cook(self, food):  
return f"The oven bakes the {food}."  
  
def can_cook(self, food):  
return food == "pizza"  
  
  
class Grill:  
  
def cook(self, food):  
return f"The grill sears the {food}."  
  
def can_cook(self, food):  
return food == "burgers"  
  
def cooking_method(self):  
return "direct heat"  
  
  
and  
  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
test_grill_can_cook_burgers (\_\_main\_\_.TestCookingAppliance.test_grill_can_cook_burgers) ... ok  
test_grill_cannot_cook_cake (\_\_main\_\_.TestCookingAppliance.test_grill_cannot_cook_cake) ... ok  
test_grill_reports_direct_heat (\_\_main\_\_.TestCookingAppliance.test_grill_reports_direct_heat) ... ok  
test_grill_sears_bread (\_\_main\_\_.TestCookingAppliance.test_grill_sears_bread) ... ok  
test_oven_bakes_bread (\_\_main\_\_.TestCookingAppliance.test_oven_bakes_bread) ... ok  
test_oven_can_cook_pizza (\_\_main\_\_.TestCookingAppliance.test_oven_can_cook_pizza) ... ok  
  
----------------------------------------------------------------------  
Ran 6 tests in 0.000s  
  
OK  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> git diff -- .\cooking_appliance.py  
diff --git a/week_06/unit_testing_example/cooking_appliance.py b/week_06/unit_testing_example/cooking_appliance.py  
index 9c9541f..5d7cb90 100644  
--- a/week_06/unit_testing_example/cooking_appliance.py  
+++ b/week_06/unit_testing_example/cooking_appliance.py  
@@ -10,4 +10,11 @@ class Oven:  
class Grill:  
  
def cook(self, food):  
- return f"The grill sears the {food}."  
\\ No newline at end of file  
+ return f"The grill sears the {food}."  
+  
+ def can_cook(self, food):  
+ return food == "burgers"  
+  
+ def cooking_method(self):  
+ return "direct heat"  
+  
\\ No newline at end of file  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
okay. what do you want to see now?

## **Copilot:**

Nice. You jumped ahead and made \*\*all three failing tests Green\*\*, and your evidence is solid:  
  
- Six tests pass.  
- \`Grill.can_cook("burgers")\` returns \`True\`.  
- \`Grill.can_cook("cake")\` returns \`False\`.  
- \`Grill.cooking_method()\` returns \`"direct heat"\`.  
- \`git diff\` shows exactly what changed.  
  
\## What I want to see next  
  
Now we need a test that asks the actual Week 6 question:  
  
\> Can the same operation be sent to both appliances while each behaves differently?  
  
We already suspect the shared operation is:

cook(food)

Our next test should place both appliances in the same collection, call \`cook()\` without checking their types, and verify different outcomes.  
  
\### First, preserve this Green checkpoint

git add .\cooking_appliance.py . est_cooking_appliance.py  
git commit -m "Add tested grill capabilities"

Then open the test file:

code . est_cooking_appliance.py

Before adding inheritance, our next Red test will introduce a shared function named:

prepare_meal(appliance, food)

It will receive either appliance and send the same \`cook()\` message. That takes us from merely having similar classes toward proving genuine substitution.  
  
One cleanup note: Git reports:

No newline at end of file

That is not breaking anything. In VS Code, place the cursor after the final line and press \*\*Enter\*\* once before saving.

## **Jeremy:**

Before adding inheritance, our next Red test will introduce a shared function named:  
Python  
prepare_meal(appliance, food)  
Show more lines  
It will receive either appliance and send the same \<code spellcheck="false" data-lexical-text="true"\>cook()\</code\> message. That takes us from merely having similar classes toward proving genuine substitution.  
  
please reword this and exmplain it more clearly.  
  
and then give us a one for one drop in replacement  
  
import unittest  
  
from cooking_appliance import Grill, Oven  
  
  
class TestCookingAppliance(unittest.TestCase):  
  
def test_oven_bakes_bread(self):  
oven = Oven()  
  
result = oven.cook("bread")  
  
self.assertEqual(  
result,  
"The oven bakes the bread."  
)  
  
def test_grill_sears_bread(self):  
grill = Grill()  
  
result = grill.cook("bread")  
  
self.assertEqual(  
result,  
"The grill sears the bread."  
)  
  
def test_oven_can_cook_pizza(self):  
oven = Oven()  
  
result = oven.can_cook("pizza")  
  
self.assertTrue(result)  
  
def test_grill_can_cook_burgers(self):  
grill = Grill()  
  
result = grill.can_cook("burgers")  
  
self.assertTrue(result)  
  
def test_grill_cannot_cook_cake(self):  
grill = Grill()  
  
result = grill.can_cook("cake")  
  
self.assertFalse(result)  
  
def test_grill_reports_direct_heat(self):  
grill = Grill()  
  
result = grill.cooking_method()  
  
self.assertEqual(  
result,  
"direct heat"  
)  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)

## **Copilot:**

Right now, \`Oven\` and \`Grill\` happen to use the same method name, \`cook()\`. Our next test asks whether another part of the program can use \*\*either appliance without needing to know which one it received\*\*.  
  
The proposed \`prepare_meal(appliance, food)\` function will:  
  
1. Receive an appliance as an argument.  
2. Call \`appliance.cook(food)\`.  
3. Trust the object to perform the appropriate behavior.  
  
If it receives an \`Oven\`, the food is baked. If it receives a \`Grill\`, the food is seared. The function does not use an \`if\` statement to determine the appliance type. That is the beginning of \*\*substitution and polymorphism\*\*.  
  
For this step, change only the test file. The new test should fail because \`prepare_meal()\` does not exist yet.  
  
\## Drop-in replacement for \`test_cooking_appliance.py\`  
  
Open the file:

code . est_cooking_appliance.py

Replace its entire contents with:

import unittest  
  
from cooking_appliance import Grill, Oven, prepare_meal  
  
  
class TestCookingAppliance(unittest.TestCase):  
  
def test_oven_bakes_bread(self):  
oven = Oven()  
  
result = oven.cook("bread")  
  
self.assertEqual(  
result,  
"The oven bakes the bread."  
)  
  
def test_grill_sears_bread(self):  
grill = Grill()  
  
result = grill.cook("bread")  
  
self.assertEqual(  
result,  
"The grill sears the bread."  
)  
  
def test_oven_can_cook_pizza(self):  
oven = Oven()  
  
result = oven.can_cook("pizza")  
  
self.assertTrue(result)  
  
def test_grill_can_cook_burgers(self):  
grill = Grill()  
  
result = grill.can_cook("burgers")  
  
self.assertTrue(result)  
  
def test_grill_cannot_cook_cake(self):  
grill = Grill()  
  
result = grill.can_cook("cake")  
  
self.assertFalse(result)  
  
def test_grill_reports_direct_heat(self):  
grill = Grill()  
  
result = grill.cooking_method()  
  
self.assertEqual(  
result,  
"direct heat"  
)  
  
def test_prepare_meal_uses_each_appliances_cook_behavior(self):  
appliances = \[  
Oven(),  
Grill(),  
\]  
  
results = \[  
prepare_meal(appliance, "corn")  
for appliance in appliances  
\]  
  
self.assertEqual(  
results,  
\[  
"The oven bakes the corn.",  
"The grill sears the corn.",  
\]  
)  
  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)

Save it and run:

python . est_cooking_appliance.py

\## Expected Red result  
  
The file will probably stop during the import with:

ImportError: cannot import name 'prepare_meal' from 'cooking_appliance'

That is the intended Red result. The test is requesting a shared calling path that does not exist yet.  
  
\## What the new test will eventually prove  
  
This part supplies different objects to the same operation:

prepare_meal(appliance, "corn")

The caller does not say:

if isinstance(appliance, Oven):

Instead, it trusts each appliance to understand:

cook("corn")

The expected results show different behavior:

\[  
"The oven bakes the corn.",  
"The grill sears the corn.",  
\]

This does \*\*not yet prove that inheritance is required\*\*. It first proves the more important fact: \`Oven\` and \`Grill\` already support meaningful substitution through their shared \`cook()\` operation.

## **Jeremy:**

class Oven:  
  
def cook(self, food):  
return f"The oven bakes the {food}."  
  
def can_cook(self, food):  
return food == "pizza"  
  
  
class Grill:  
  
def cook(self, food):  
return f"The grill sears the {food}."  
  
def can_cook(self, food):  
return food == "burgers"  
  
def cooking_method(self):  
return "direct heat"  
  
  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\> python .\test_cooking_appliance.py  
Traceback (most recent call last):  
File "C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\test_cooking_appliance.py", line 3, in \<module\>  
from cooking_appliance import Grill, Oven, prepare_meal  
ImportError: cannot import name 'prepare_meal' from 'cooking_appliance' (C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\cooking_appliance.py)  
PS C:\Users\<you>\git\computer_science_2\week_06\unit_testing_example\>  
  
  
now what do we change.

## **Copilot:**

Exactly. The test is Red because \`prepare_meal\` does not exist. Now we make the \*\*smallest implementation change\*\* needed to pass it.  
  
Change only \`cooking_appliance.py\`. Leave the tests untouched.  
  
\## Open the implementation file

code .\cooking_appliance.py

Replace the entire file with:

class Oven:  
  
def cook(self, food):  
return f"The oven bakes the {food}."  
  
def can_cook(self, food):  
return food == "pizza"  
  
  
class Grill:  
  
def cook(self, food):  
return f"The grill sears the {food}."  
  
def can_cook(self, food):  
return food == "burgers"  
  
def cooking_method(self):  
return "direct heat"  
  
  
def prepare_meal(appliance, food):  
return appliance.cook(food)

Save it, then run:

python . est_cooking_appliance.py

\## What the new function does

def prepare_meal(appliance, food):  
return appliance.cook(food)

Notice that it does \*\*not\*\* ask whether the appliance is an \`Oven\` or a \`Grill\`. It simply trusts the supplied object to have a working \`cook()\` method.  
  
When given:

prepare_meal(Oven(), "corn")

Python runs \`Oven.cook()\`.  
  
When given:

prepare_meal(Grill(), "corn")

Python runs \`Grill.cook()\`.  
  
The caller uses one operation, while each object supplies its own behavior. That is the substitution behavior we wanted to prove.  
  
\## Expected result  
  
You should now have seven passing tests:

Ran 7 tests  
  
OK

We still have not added inheritance. The test first proves that the shared operation works. Inheritance, if we add it, should make an already-demonstrated relationship explicit rather than inventing one.

## **Jeremy:**

"give me a durable artifact, a summary of this conversation"

## **Copilot:**

I created a durable Markdown artifact summarizing the complete TDD walkthrough, including the Red-Green progression, current code, test suite, Git evidence, design reasoning, World Bible entry, and AI accountability receipt.  
  
\[The original reply included a generated-file download citation.\]  
  
Suggested repository location:

week_06/unit_testing_example/week_06_tdd_unit_testing_conversation_summary.md

After downloading it into that folder:

git add .\week_06_tdd_unit_testing_conversation_summary.md  
git commit -m "Document Week 6 TDD unit testing walkthrough"  
git status

## **Jeremy:**

I want to archive this entire conversation as a Word document. Please create a Word (.docx) file now.  
  
What to include  
1. The full conversation history, as complete and verbatim as you can manage. This is a transcript, not a summary. Include every one of my messages and every one of your replies, in order, labeled "Jeremy:" and "Copilot:".  
2. Keep all code blocks, commands, file names, tables and lists exactly as they appeared, with code in a monospaced font.  
3. If something is too long to fit, keep it anyway, and don't paraphrase or shorten it. If you truly cannot include some part, add a clear note saying what was left out and why.  
4. At the very top, add a short header with:  
- the conversation topic  
- today's date  
- the course (CS1, CS2, Discrete Structures, or "none")  
- a one-paragraph summary  
5. At the very end, add a short list of key decisions, final answers, and any code or examples worth reusing.  
  
Rules  
- Do not include student names, grades, student submissions, or anything from student email. If any appears in this conversation, replace it with "\[student info removed\]" and tell me in your reply that you did so.  
- Don't invent or improve content. If you're unsure about something, include what was actually said.  
  
File name  
Use this pattern: YYYY-MM-DD_COURSE_short-topic.docx. For example, 2026-10-09_CS2_queues-and-stacks.docx. Use "NONE" if there is no course.  
  
Output  
Create the actual Word file and give me the download link. Then tell me exactly where it was saved (the OneDrive folder path) if you know it. If you don't know, say so rather than guessing.

# Key Decisions, Final Answers, and Reusable Material

- Use the TDD loop Red, Green, Refactor, and make one bounded change at a time.

- Do not introduce inheritance merely because two classes look similar. First prove meaningful substitution through a shared operation.

- Oven and Grill both receive cook(food), but Oven bakes and Grill sears.

- Use prepare_meal(appliance, food) to demonstrate that the same caller can use either object without checking its concrete type.

- Use python .\test_cooking_appliance.py to run the unittest suite.

- Use git diff -- .\cooking_appliance.py .\test_cooking_appliance.py to preserve a review receipt.

- Reusable implementation: def prepare_meal(appliance, food): return appliance.cook(food)

- Reusable World Bible decision: tests demonstrate shared cook(food) substitution; an explicit parent contract remains a future design decision rather than an assumed requirement.
