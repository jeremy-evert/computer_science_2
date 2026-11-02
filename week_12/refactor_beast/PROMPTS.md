# Prompts for the Beast (paste one at a time into your AI chat)

Goal: make things that work better and are easier to manage, without breaking them.
Rules for the whole session: **one prompt at a time. Run the tests after every change. Red means undo.** You read what the AI proposes before you accept it, and you can explain each change in one sentence.

Attach `beast.py` (paste its contents) when a prompt says "the code".

---

## 01. Taking stock: what do we have?

```
I'm going to give you a Python program. Do NOT change anything yet.
Tell me, in plain language:
1. What does this program do, start to finish?
2. List every function and what it does in one line.
3. List every global variable and which functions change it.
4. What files does it write, and which of those would be different if I run it twice?
Then ask me any questions you need before we go further.

[paste beast.py]
```

You check: did it find the globals (`C`, `S`, `P`, `R`)? Did it notice `timings.csv` changes every run?

## 02. Draw the "before" map

```
Make me a simple map of this program as it is now: a diagram showing which functions call which, and which global variables they share. Use Mermaid (flowchart) so I can paste it into a viewer. Don't suggest improvements yet. Just show what is there.
```

You check: save this as your "before" map. Does it match what you saw in prompt 01?

## 03. Lock in the baseline

```
I want to save what this program does today so I can tell later if I broke it.
Give me exact commands to: run the program, copy out/sort_counts.csv, out/search_counts.csv and out/report.tex into a folder called baseline/, and explain why I should NOT copy timings.csv or the PDF.
```

You check: run it twice. Do the three baseline files stay identical? If not, stop and ask why.

## 04. Lock in the small pieces: unit tests

```
Using pytest, write tests for these functions in beast.py: lin, binr, bs, ins, sel.
- Each sort: gives a sorted list for an empty list, one item, already sorted, reversed, and a list with duplicates.
- lin and binr: find an item that is present, report -1 for one that is missing.
- Counting: for the list [3, 1, 2], tell me by hand what comparisons and swaps each sort should report, then test that.
Do NOT change beast.py. If a test fails, tell me whether the test or the code is wrong and why.
```

You check: run `pytest`. Do all pass? Read one test aloud and say what it protects.

## 05. Lock in the whole program: a characterization test

```
Write one more pytest test that runs the whole program and checks that out/sort_counts.csv, out/search_counts.csv and out/report.tex are exactly the same as the files in baseline/. It should run in a temporary folder so it doesn't touch my real out/ folder. It must ignore timings.csv. Do NOT change beast.py.
```

You check: it passes now. Then change one number in `beast.py` on purpose (like `T = 5` to `T = 4`) and see the test fail. Change it back. That red test is what protects you.

## 06. Refactor the tests

```
Here are my tests. Don't change beast.py. Make the tests easier to read and maintain:
- remove repeated code (use pytest fixtures and parametrize),
- give each test a name that says what it protects,
- keep exactly the same coverage. After the change, the same number of cases must still be checked.
Show me the diff and tell me what each change buys me.

[paste your tests]
```

You check: run `pytest`. Same behavior, fewer lines?

## 07. Refactor the code, step 1: get rid of the global counters

```
Look at the global variables C, S and P in beast.py. Propose ONE small change that removes them, for example by having each sort return its counts, or by passing in a small counter object. Change only that. Show me the diff. Don't touch anything else.
```

You check: `pytest`. All green? If red, undo it and read the failure. What did the tests catch?

## 08. Refactor the code, step 2: separate computing from writing files

```
Now split the big go() function. Make one change: pull the part that runs the experiments out of go() into its own function that returns the results and writes no files. Leave the file-writing where it is for now. Show me the diff. One step only.
```

You check: `pytest`. Does the program still write byte-identical CSVs and report.tex?

## 09. Refactor the code, step 3: make the LaTeX a helper

```
The LaTeX report is built by gluing strings together inside go(). Move the report building into a function (or two) that takes the results and returns the text, and write one small test for it. Keep the output identical. One step only.
```

You check: the whole-program test is still green.

## 10. Rerun, compare, and look at the after map

```
Give me the commands to rerun the program and diff its output against baseline/. Then draw the "after" map of the program, in the same Mermaid style as before, so I can compare the two. Finally, list every difference between the two maps.
```

You check: nothing changed in the output that you didn't choose. Save the after map next to the before map.

## 11. Look back (your four sentences)

```
Help me think, but do not write it for me: ask me four questions that lead me to write (1) what I changed, (2) what the tests caught, (3) one thing I chose NOT to change and why, and (4) what I would do with another hour.
```

You check: write the four sentences yourself.

---

Bonus, if there is time:
- `binr` counts two probes per loop. Is that a bug? What would you change in the baseline, and what would you tell the next reader?
- Remove one duplicate (`bs` vs `bs2`). Which tests would you need before you dared?
