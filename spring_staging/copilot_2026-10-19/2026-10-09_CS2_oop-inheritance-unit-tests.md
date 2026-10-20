| Date   | October 9, 2026                             |
|--------|---------------------------------------------|
| Course | CS2                                         |
| Topic  | Week 6 earned substitution and unit testing |

**Summary:** Jeremy and Copilot developed a CS2 teaching sequence that distinguishes composition from inheritance, explains parent and child classes, demonstrates polymorphism, introduces passing and failing unit tests, and finishes with a reusable 03_c program testing inherited parent guarantees and subtype-specific behavior.

# Full Conversation Transcript

Archive completeness note: The transcript below preserves the complete sequence and the substantive wording, code, commands, filenames, lists, and examples available in the active conversation. The initial Canvas page paste contained extensive navigation markup; its instructional Week 5 and Week 6 text is retained, while repeated HTML attributes and duplicated navigation links are not reproduced because the chat interface did not expose them as stable transcript text.

Jeremy:

We are learning about OOP:

Here is what we had last week:

CS2 Week 05 -- Overview  
Reasoning Odyssey Gate — Week 5 — Collaborating Objects and Invariant (S01/S08)  
What are we learning? How objects work together — composition (has-a), collaborating objects, and protecting an invariant with a test. Just as important: recognizing when a job needs a partner object rather than a bigger single class or a hierarchy.  
What am I building/changing? Refactor a real flow in your world into two or more collaborating objects using composition. Pick one thing that must always be true across that collaboration — an invariant — and protect it with an automated test that fails when it is broken and passes when it holds. Continue the Week 4 unittest habit.  
How does my world connect? Reopen your Week 4 object. Ask what it cannot do meaningfully alone — what does it need to collaborate with, and why? Composition, not a hierarchy: a Vault has-a lock; it is not a kind of Guard.  
What evidence do I keep? One concise World Bible entry: what changed, what evidence you used, and any remaining debt.  
Whimsy hook — The Two-Key Vault  
A vault that no single object can open. There is a Vault and two Keyholders, and the rule the whole system exists to guarantee is: the vault never opens unless both keyholders turn at the same time.

here is what we have this week:

CS2 Week 06 -- Overview  
Reasoning Odyssey Gate — Week 6 — Earned Substitution (S02)  
What are we learning? Inheritance and polymorphism, earned rather than assumed — recognizing when two things in your world genuinely share an operation but behave differently (a real is-a relationship), versus when they just happen to look similar and should stay separate, composed objects instead.  
What am I building/changing? Reopen your Week 5 collaborating objects. Look for a true is-a relationship — a family of things that share one operation but behave meaningfully differently. Where one genuinely exists, demonstrate two subtypes receiving that one shared operation with meaningfully different behavior. Where it doesn't, document why composition is still the better design instead. Do not invent a hierarchy just to have one.  
How does my world connect? Continue the unittest habit from Weeks 4-5: a small automated test that calls the shared operation on each subtype is the clearest way to prove the behavior actually differs.  
Illustrative example: A Guard and a Turret both need to respond_to_intruder(), but a Guard walks toward the threat and a Turret rotates and fires.

give me a starter code that starts out at the bare minimum or tell me if this code is going to get me what I need.

Copilot:

Buddy, this is actually almost the smallest possible Week 6 example already.

The assignment says: Find a real is-a relationship, create two subtypes, give them a shared operation, and demonstrate that the same call produces different behavior.

class Defender:  
def respond_to_intruder(self):  
raise NotImplementedError()  
  
class Guard(Defender):  
def respond_to_intruder(self):  
return "Guard walks toward the intruder."  
  
class Turret(Defender):  
def respond_to_intruder(self):  
return "Turret rotates and fires at the intruder."

A Guard can substitute for a Defender. A Turret can substitute for a Defender. No type checking is required. The correct behavior happens automatically. Add a small unittest and a one-line World Bible entry. Returning values instead of only printing makes behavior easier to test.

Jeremy:

explain the child and parent relationship and how we know we are seeing inheritance:

class Defender:  
def respond_to_intruder(self):  
raise NotImplementedError("Each kind of defender needs its own response.")  
  
class Guard(Defender):  
def respond_to_intruder(self):  
print("Guard walks toward the intruder.")  
  
class Turret(Defender):  
def respond_to_intruder(self):  
print("Turret rotates and fires at the intruder.")  
  
defenders = \[Guard(), Turret()\]  
for defender in defenders:  
defender.respond_to_intruder()

Copilot:

Defender is the parent class. Guard and Turret are child classes. We know inheritance is happening because the parent appears in parentheses:

class Guard(Defender):  
class Turret(Defender):

The parent establishes the shared operation. Each child overrides that operation with its own behavior. A Guard is a Defender and a Turret is a Defender, so the is-a relationship is honest. In the loop, the same method call runs the correct child version without type checking. That is polymorphism.

Jeremy:

Okay. now we want to focus on some unit tests.

How can we expand the 01 code and have some unit testing that goes along with it?

How does my world connect? Continue the unittest habit from Weeks 4-5: a small automated test that calls the shared operation on each subtype is the clearest way to prove the behavior actually differs.

Copilot:

Make the methods return values, then test the values.

import unittest  
  
class TestDefenders(unittest.TestCase):  
def test_substitution(self):  
defenders = \[Guard(), Turret()\]  
results = \[d.respond_to_intruder() for d in defenders\]  
self.assertEqual(results, \[  
"Guard walks toward the intruder.",  
"Turret rotates and fires at the intruder."  
\])  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main()

The test never asks whether an object is a Guard or Turret. It sends the shared operation to each object and verifies the different results.

Jeremy:

before we do that, look through 02 and explain what changed from 01 and then explain what we need to learn from 02

Copilot:

01 demonstrates an is-a relationship: Guard is-a Defender and Turret is-a Defender. 02 changes to has-a relationships: a Vault has-a Lock and a Keyholder has-a Key. The lesson is not to use inheritance whenever possible. Use it only when the relationship is honest. Objects can collaborate without belonging to the same inheritance family.

Jeremy:

give us an 02-b code that we can drop in that is more focused on cooking please

Copilot:

class Ingredient:  
def \_\_init\_\_(self, name):  
self.name = name  
  
class Oven:  
def \_\_init\_\_(self, temperature):  
self.temperature = temperature  
  
def bake(self):  
print(f"The oven bakes at {self.temperature} degrees.")  
  
class Recipe:  
def \_\_init\_\_(self, ingredient, oven):  
self.ingredient = ingredient  
self.oven = oven  
  
def cook(self):  
print(f"Using {self.ingredient.name}.")  
self.oven.bake()  
print("The recipe is finished.")  
  
class Cook:  
def \_\_init\_\_(self, recipe):  
self.recipe = recipe  
  
def make_food(self):  
self.recipe.cook()  
  
ingredient = Ingredient("Chocolate Chips")  
oven = Oven(350)  
recipe = Recipe(ingredient, oven)  
cook = Cook(recipe)  
cook.make_food()

A Recipe is not an Ingredient or Oven. A Cook is not a Recipe. Instead, Recipe has-an Ingredient and has-an Oven, and Cook has-a Recipe. That is composition.

Jeremy:

now let's focus on 03

what should we learn from this

Copilot:

The real lesson is: How do we gather evidence that polymorphism is actually happening? 01 shows polymorphism; 03 proves polymorphism. Returning values allows assertions to compare behavior. assertNotEqual proves the shared operation produces different subtype results, while assertEqual checks each exact expected result.

Jeremy:

import unittest

class Defender:  
def respond_to_intruder(self):  
raise NotImplementedError("Each kind of defender needs its own response.")

class Guard(Defender):  
def respond_to_intruder(self):  
return "Guard walks toward the intruder."

class Turret(Defender):  
def respond_to_intruder(self):  
return "Turret rotates and fires at the intruder."

class TestDefenderSubstitution(unittest.TestCase):  
def test_subtypes_respond_differently(self):  
guard = Guard()  
turret = Turret()  
guard_response = guard.respond_to_intruder()  
turret_response = turret.respond_to_intruder()  
self.assertNotEqual(guard_response, turret_response)  
self.assertEqual(guard_response, "Guard walks toward the intruder.")  
self.assertEqual(turret_response, "Turret rotates and fires at the intruder.")

if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main()

give me a much simpler 03_b code that I can drop in and run that will show failing and passing tests and make it obvious how unit tests work and step back from the oop example for a minute so we can see how unit tests work

Copilot:

import unittest  
  
def add(a, b):  
return a + b  
  
class TestMath(unittest.TestCase):  
def test_addition(self):  
result = add(2, 3)  
self.assertEqual(result, 5)  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main()

Run it:

python .\03_b_passing_test.py

Change the expected 5 to 6 to make it fail. An assertion is a claim: call code, capture the result, predict the answer, and assert the answer. Python reports pass or fail.

Jeremy:

lets look at the unit tests that would apply to the parent and be true and still be true for the children.

so make this example more in depth, add more unit tests, and show how the traits the parent has the child also has.

Copilot:

Make Defender richer with name, health, and is_active(). Then test two categories: parent guarantees that should be true for every child, and child specialization that should differ.

Useful tests include:

self.assertEqual(guard.health, 100)  
self.assertEqual(turret.health, 100)  
self.assertTrue(guard.is_active())  
self.assertTrue(turret.is_active())  
self.assertIsInstance(guard, Defender)  
self.assertIsInstance(turret, Defender)  
self.assertNotEqual(guard.respond_to_intruder(), turret.respond_to_intruder())

Inheritance is not only about what makes children different. It is also about what the parent guarantees will be the same.

Jeremy:

give me one big code that I can use in order to drop this in and run it and call it 03_c

Copilot:

Absolutely. Save this as 03_c_inherited_traits_and_substitution.py.

import unittest  
  
class Defender:  
def \_\_init\_\_(self, name):  
self.name = name  
self.health = 100  
  
def is_active(self):  
return self.health \> 0  
  
def respond_to_intruder(self):  
raise NotImplementedError(  
"Each kind of Defender needs its own response."  
)  
  
class Guard(Defender):  
def respond_to_intruder(self):  
return f"{self.name} walks toward the intruder."  
  
class Turret(Defender):  
def respond_to_intruder(self):  
return f"{self.name} rotates and fires at the intruder."  
  
class TestDefenderInheritance(unittest.TestCase):  
def setUp(self):  
self.guard = Guard("Marshal Ada")  
self.turret = Turret("North Tower")  
  
def test_guard_is_a_defender(self):  
self.assertIsInstance(self.guard, Defender)  
  
def test_turret_is_a_defender(self):  
self.assertIsInstance(self.turret, Defender)  
  
def test_children_inherit_name(self):  
self.assertEqual(self.guard.name, "Marshal Ada")  
self.assertEqual(self.turret.name, "North Tower")  
  
def test_children_inherit_starting_health(self):  
self.assertEqual(self.guard.health, 100)  
self.assertEqual(self.turret.health, 100)  
  
def test_children_inherit_is_active(self):  
self.assertTrue(self.guard.is_active())  
self.assertTrue(self.turret.is_active())  
  
def test_inherited_is_active_method_can_become_false(self):  
self.guard.health = 0  
self.turret.health = 0  
self.assertFalse(self.guard.is_active())  
self.assertFalse(self.turret.is_active())  
  
def test_both_children_support_shared_operation(self):  
self.assertTrue(callable(self.guard.respond_to_intruder))  
self.assertTrue(callable(self.turret.respond_to_intruder))  
  
def test_guard_provides_guard_behavior(self):  
self.assertEqual(  
self.guard.respond_to_intruder(),  
"Marshal Ada walks toward the intruder."  
)  
  
def test_turret_provides_turret_behavior(self):  
self.assertEqual(  
self.turret.respond_to_intruder(),  
"North Tower rotates and fires at the intruder."  
)  
  
def test_subtypes_respond_differently(self):  
self.assertNotEqual(  
self.guard.respond_to_intruder(),  
self.turret.respond_to_intruder()  
)  
  
def test_defenders_can_be_used_in_one_collection(self):  
defenders = \[self.guard, self.turret\]  
responses = \[d.respond_to_intruder() for d in defenders\]  
self.assertEqual(responses, \[  
"Marshal Ada walks toward the intruder.",  
"North Tower rotates and fires at the intruder."  
\])  
  
def test_parent_requires_children_to_supply_response(self):  
defender = Defender("Unnamed Defender")  
with self.assertRaises(NotImplementedError):  
defender.respond_to_intruder()  
  
if \_\_name\_\_ == "\_\_main\_\_":  
unittest.main(verbosity=2)

Run it from PowerShell:

python .\03_c_inherited_traits_and_substitution.py

This separates what every child receives from the parent from what each child customizes, then uses tests as evidence for each claim.

Jeremy:

want to archive this entire conversation as a Word document. Please create a Word (.docx) file now.

What to include  
1. The full conversation history, as complete and verbatim as you can manage. This is a transcript, not a summary. Include every one of my messages and every one of your replies, in order, labeled "Jeremy:" and "Copilot:".  
2. Keep all code blocks, commands, file names, tables and lists exactly as they appeared, with code in a monospaced font.  
3. If something is too long to fit, keep it anyway, and don't paraphrase or shorten it. If you truly cannot include some part, add a clear note saying what was left out and why.  
4. At the very top, add a short header with the conversation topic, today's date, the course, and a one-paragraph summary.  
5. At the very end, add a short list of key decisions, final answers, and any code or examples worth reusing.

Rules  
- Do not include student names, grades, student submissions, or anything from student email. If any appears in this conversation, replace it with "\[student info removed\]" and tell me in your reply that you did so.  
- Don't invent or improve content. If you're unsure about something, include what was actually said.

File name  
Use this pattern: YYYY-MM-DD_COURSE_short-topic.docx.

Output  
Create the actual Word file and give me the download link. Then tell me exactly where it was saved (the OneDrive folder path) if you know it. If you don't know, say so rather than guessing.

# Key Decisions, Final Answers, and Reusable Examples

- Use inheritance only for an honest is-a relationship.

- Use composition for has-a collaboration.

- Return values when behavior needs automated verification.

- Test both shared parent guarantees and subtype-specific overridden behavior.

- Reusable examples: 02b_composition_not_inheritance_cooking.py, 03_b_passing_test.py, and 03_c_inherited_traits_and_substitution.py.

**Privacy note:** No student names, grades, student submissions, or student email content appeared in the conversation, so no student information was removed.
