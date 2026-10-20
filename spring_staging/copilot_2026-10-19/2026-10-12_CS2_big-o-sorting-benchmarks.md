**CS2 Week 9: Big O, Sorting, Searching, and Benchmarking**

Starship Data Log -- Reasoning Odyssey Gate, Week 9 (Search/Order Tradeoff)

*Session archive -- Monday, October 12, 2026 -- Jeremy Evert, SWOSU*

1\. What We Set Out to Do

The goal of this session was to explore Big O, sorting, searching, and benchmarking with real measurements from the classroom machine, using the Starship Data Log world. The guiding question: when does it make sense to sort first, and when should we just search the unsorted data?

The Week 9 gate asks students to reopen their Week 8 structure (not build a new one), trace a lookup or ordering operation over real world state, name any sorted-data precondition, explain a plain-language cost/maintenance tradeoff, and keep one concise World Bible entry. Binary search should only appear if the world earns it.

|                                          |            |                                                                 |
|------------------------------------------|------------|-----------------------------------------------------------------|
| **Rubric criterion**                     | **Points** | **Meets expectation**                                           |
| Real lookup/order fit                    | 8          | Operation is meaningful for the world, over real state          |
| Trace and precondition                   | 7          | A trace/test demonstrates it; sorted-data precondition is named |
| Cost/maintenance reasoning / World Bible | 6          | Qualitative tradeoff in plain language                          |
| AI accountability                        | 4          | Proposal, diff, independent test, reasoning, accept/reject      |

2\. Workflow: Copilot Writes Prompts, Claude Code Builds

Early on we clarified the division of labor: Copilot writes the prompts, and Claude Code on the classroom machine writes, runs, commits, and pushes the code. Each step below shows the prompt (condensed) and what Claude Code reported back.

2.1 Prompt: Week 9 gate file

You are helping a CS2 professor build a Week 9 gate artifact for a course called

"Reasoning Odyssey." The theme world is a Starship Data Log. Reopen the Week 8

structure (a queue or list of starship sensor log entries) and extend it to

demonstrate sorting and searching tradeoffs.

GOAL: Build week_09_gate.py that:

1\. WORLD DATA: 1000 random StarshipLogEntry objects (entry_id, timestamp,

severity 1-5, message chosen from 8-10 plausible starship alerts).

2\. SEARCHING: linear_search (unsorted) vs binary_search (sorted by entry_id),

timed with time.perf_counter() over 200 random lookups.

3\. SORTING: bubble_sort (O(n^2)), merge_sort (O(n log n)), python sort baseline.

4\. TRADEOFF SUMMARY: when linear search on unsorted data is fine, when sorting

first pays off, and the break-even intuition (sort once + k binary searches

vs k linear searches).

5\. WORLD BIBLE ENTRY: what changed from Week 8, evidence, remaining debt.

6\. ASSERTIONS: linear finds known target; binary finds known target;

binary returns -1 for a missing target.

CONSTRAINTS: stdlib only; bubble_sort works on a copy; classroom-readable

output; header comment with file name, purpose, week, course (CS2).

Show me the full file when done.

2.2 Prompt: Hardware profile

Extend week_09_gate.py to capture and print a hardware profile at the top of

every run (stdlib only). Add hardware_profile() that prints:

1\. CPU: platform.processor(), platform.machine(), platform.system()/release(),

os.cpu_count()

2\. Python: sys.version, sys.executable

3\. CPU loop proxy: count loop iterations for 0.5 s, report iterations/second

4\. Memory: peak memory of this process, free physical memory (fail gracefully)

5\. Run timestamp: datetime.datetime.now().isoformat()

Format as === HARDWARE PROFILE === printed BEFORE benchmark results.

Add to the World Bible entry:

"Hardware: \<processor\> \| \<cpu_count\> cores \| Run: \<timestamp\>"

Do a full file replacement.

2.3 What came back: machine profile and lookup results

Claude Code found that week_09_gate.py did not yet exist, so it created it. It also replaced wmic (removed from Windows 11) with a ctypes approach and kept wmic only as a fallback. The summary was saved as week_09/BENCHMARK_RESULTS.md and pushed to origin/main.

|                                         |                                                                |
|-----------------------------------------|----------------------------------------------------------------|
| **Item**                                | **Measured value**                                             |
| CPU                                     | 13th Gen Intel Core i7-13700 (16 cores, 24 logical processors) |
| OS / Python                             | Windows 11, Python 3.12.10                                     |
| CPU loop proxy                          | about 20.6 million iterations/second                           |
| Free memory / script peak               | about 4.07 GB free / about 20 MB peak                          |
| Linear search, 200 lookups, n = 100,000 | about 0.30 s                                                   |
| Sort once                               | about 0.014 s                                                  |
| Bisect, 200 lookups on sorted data      | about 0.0001 s                                                 |
| Sort + bisect total                     | about 0.014 s -- sorting first wins at 200 lookups             |

**Takeaway:** with 200 lookups, paying once for a sort and then using binary search was roughly 20x cheaper than repeated linear scans. With only one or two lookups, the linear scan wins because there is no sort cost to pay off. The sorted-data precondition is what makes binary search legal.

3\. Bubble Sort and the O(n²) Curve

3.1 What bubble sort is

Bubble sort walks the list repeatedly and swaps any two neighbors that are out of order. After each pass, the largest remaining value has "bubbled" to the end. It stops when a pass makes no swaps.

Pass 1: \[5, 3, 8, 1\] -\> \[3, 5, 1, 8\] (8 bubbled to the end)

Pass 2: \[3, 5, 1, 8\] -\> \[3, 1, 5, 8\]

Pass 3: \[3, 1, 5, 8\] -\> \[1, 3, 5, 8\] done

In the worst case it makes about n passes of up to n comparisons each, so the work grows like n². Double n and the work quadruples; triple n and it grows ninefold. It is rarely used in production but is ideal for teaching because the quadratic curve is so visible.

3.2 Prompt: Bubble sort benchmark

Create week_09/bubble_sort_benchmark.py (stdlib only; do not break existing files).

1\. bubble_sort, merge_sort, python_sort (sorted) -- copies only.

2\. SCALING BENCHMARK at n = \[100, 250, 500, 1000, 2500, 5000, 10000, ...\]

seed = 42 + n. Stop growing bubble sort once a run would exceed 120 s;

keep running merge and python sort. Print a halt note.

3\. RESULTS TABLE: n \| bubble \| merge \| python \| bubble/python ratio

4\. BIG O REALITY CHECK for consecutive n pairs: actual bubble ratio vs

(n2/n1)^2, actual merge ratio vs (n2 log n2)/(n1 log n1).

5\. WHAT THIS TELLS US: 4-6 plain sentences.

6\. ASSERTIONS before the benchmark.

7\. HARDWARE HEADER. 8. WORLD BIBLE ENTRY.

Save output to week_09/BUBBLE_SORT_RESULTS.md, then git add / commit / push

origin main. Show me the full file when done.

3.3 What came back

- Largest list bubble sort finished within two minutes: n = 60,000, in about 109 s.

- n = 80,000 was projected at about 193 s and skipped.

- Away from the noisy rows, measured ratios tracked n² cleanly: about 4.0 per doubling.

- Claude Code added bubble_sort_results.json, bubble_sort_report.py (seaborn/matplotlib), and an HTML report at week_09/report/index.html.

- Caveat it reported: pip install ran during the benchmark, distorting the n = 30,000 to 40,000 rows (35 s vs 23.8 s in an earlier run).

<img src="media/83e642d39e854e171ea3c74de622bf38b79dd6c2.png" title="Bubble sort time vs n" style="width:5.83333in;height:3.5625in" alt="Bubble sort time vs n" />

*Figure 1. Bubble sort seconds vs. input size, with the 120 s budget line.*

<img src="media/7c1856a43a7fa75dc613f7ea2f3b8163404673bb.png" title="Log-log comparison" style="width:5.83333in;height:3.5625in" alt="Log-log comparison" />

*Figure 2. Log-log: bubble (slope about 2) vs. merge sort and sorted() (slope just above 1).*

4\. "We Got Lied To" -- Timing Variance

The chart has a kink around n = 30,000. Bubble sort is O(n²), but the machine is not a perfect O(n²) instrument. Reading the plotted points:

|                |                           |                 |                                             |
|----------------|---------------------------|-----------------|---------------------------------------------|
| **Transition** | **Approx. actual ratio**  | **Theory (n²)** | **Verdict**                                 |
| 5k -\> 10k     | about 4.0                 | 4.00            | tracks theory                               |
| 10k -\> 20k    | about 4.0                 | 4.00            | tracks theory                               |
| 20k -\> 30k    | about 3.4 (10 s -\> 35 s) | 2.25            | too high (pip install interference)         |
| 30k -\> 40k    | about 1.3 (35 s -\> 45 s) | 1.78            | looks too low only because 30k was inflated |

One inflated point damages two ratios: the one going into it and the one coming out of it. Notice the same kink appears in the merge sort and sorted() lines on the log-log chart, which is strong evidence the cause was the machine, not the algorithm.

4.1 Prompt: Variance study

Create week_09/variance_study.py (stdlib only).

PURPOSE: Run bubble sort REPEATEDLY on the SAME list at n = 5,000 / 10,000 / 30,000

(20 trials each) so any spread in timing is machine noise, not data variance.

For each n print: min/max (with trial \#), mean, median, std dev,

coefficient of variation (CV% = std/mean\*100), range, and all raw trial times.

Show progress dots. Then print === WHY THE NUMBERS LIE === (prose):

OS scheduling, cache warm-up, thermal/turbo behavior, garbage collection,

and why a fixed-size interruption is a LARGER fraction of a SHORT run.

Print a comparison table (n \| mean \| CV% \| interpretation), a World Bible

entry, save variance_study_results.json, write VARIANCE_STUDY_RESULTS.md,

then git add / commit / push origin main.

4.2 Why the numbers vary

- **OS scheduling:** the OS can pause the process to run other work (interrupts, antivirus, updates, a pip install).

- **Cache warm-up:** early trials may run slower until data and code are hot in cache.

- **Turbo and thermal behavior:** clock speed changes with load and temperature (Task Manager showed 4.17 GHz on a 2.10 GHz base).

- **P-cores vs. E-cores:** the i7-13700 is a hybrid chip; a run scheduled onto an efficiency core is slower.

- **Garbage collection:** Python may pause briefly to collect memory.

**Coefficient of variation (CV) intuition:** a fixed-size interruption (say 5 ms) is a large fraction of a short run but a tiny fraction of a long run, so short runs tend to have higher CV%. A long, sustained interference -- like pip install -- is different: it can distort a long run substantially, which is what happened at n = 30,000.

**Correction for the record:** the variance prompt as originally written contained a self-correcting "wait, actually it is the opposite" passage about CV. The bullet above is the clean, correct version and is what students should see.

5\. Watching the CPU

htop in WSL showed every core at 0% while the benchmark ran. That is expected: Claude Code launched the benchmark with Windows Python, and htop inside WSL only sees Linux processes inside the WSL VM. To see the job, use Windows Task Manager or PowerShell (Get-Process python\*), or run the script inside WSL.

<img src="media/8ebc162ea32683a4dad4521f53e142ce9a6ebc61.png" title="Task Manager CPU view" style="width:5.83333in;height:3.11458in" alt="Task Manager CPU view" />

*Figure 3. Task Manager during the run: about 9% total utilization on 24 logical processors.*

Interpreting the 9%: one fully busy logical processor out of 24 is about 4.2%. The rest of the 9% is other system activity, plus Windows may move the single thread between cores. Bubble sort is a single-threaded Python loop, so it cannot use the other cores. To see this clearly, right-click the CPU graph and choose Change graph to \> Logical processors.

**Correction for the record:** during the session Copilot said 9% / 24 meant exactly one core at 100%; that arithmetic was off (about 4.2% is one core). Copilot also named a Python 3.13 path for the running process without evidence; the benchmark machine reported Python 3.12.10.

|             |                         |                                                             |
|-------------|-------------------------|-------------------------------------------------------------|
| **Layer**   | **What is slow**        | **Why**                                                     |
| Algorithm   | O(n²) comparisons       | Every pass walks the list                                   |
| Language    | Interpreted Python loop | Each comparison/swap is many bytecode steps                 |
| Parallelism | One core                | A plain single-threaded script; the GIL also limits threads |

6\. Bubble Sort vs. the Built-in Sort (Timsort)

Python’s sorted() and list.sort() use Timsort, a hybrid of merge sort and insertion sort designed by Tim Peters for Python. It is O(n log n) in the worst case and close to O(n) on data that is already sorted or nearly sorted, because it detects existing ordered runs. It is implemented in C, which gives it a much smaller constant factor than a Python loop.

On a log-log chart, O(n²) shows a slope of 2, and O(n log n) shows a slope just above 1. Doubling n under n log n slightly more than doubles the work, because log₂(2n) = log₂(n) + 1.

6.1 Prompt: Timsort vs. bubble

Create week_09/timsort_vs_bubble.py (do not modify existing files).

1\. bubble_sort(data) and timsort(data) = sorted(data).

2\. THREE scenarios per n: RANDOM (seed 42+n), NEARLY SORTED (2% of elements

swapped, seed 99+n), REVERSE SORTED.

3\. n = \[100, 500, 1000, 2500, 5000, 10000, 20000, 50000, 100000\];

halt bubble sort for larger sizes once a RANDOM run exceeds 30 s.

4\. One results table per scenario: n \| bubble \| timsort \| speedup.

5\. BIG O REALITY CHECK (random): actual vs theoretical ratios for n^2 and

n log n, percent off, and average percent off for each algorithm.

6\. TIMSORT scenario comparison (random vs nearly sorted vs reverse).

7\. WHAT BIG O IS REALLY SAYING: 8-10 sentences of prose.

8\. ASSERTIONS. 9. HARDWARE HEADER. 10. WORLD BIBLE ENTRY.

11\. Save timsort_results.json.

12\. Report: timsort_vs_bubble_loglog.png and speedup.png in week_09/report/,

appended as new sections to week_09/report/index.html.

Save output as week_09/TIMSORT_RESULTS.md, then git add / commit / push

origin main. Show me the full file when done.

Status at the end of this session: this prompt was written but its results were not yet reported back.

7\. Talking Points for Students

- Big O predicts how cost grows, not how fast a single run is.

- Measured ratios near 4.0 per doubling are evidence that Big O is a real prediction.

- The sorted-data precondition is what makes binary search legal; sorting costs time once.

- Sort first when you will search many times; scan unsorted data for one-off lookups or tiny n.

- Benchmarks measure the algorithm AND the machine. Repeat runs, report spread, and keep the machine quiet.

- Same Big O class does not mean same speed: constants, language, and cache behavior matter.

8\. World Bible Entry (Week 9)

- **What changed:** Starship log gained lookup and ordering operations, plus hardware-stamped benchmarks.

- **Evidence:** linear 0.30 s vs. sort + bisect 0.014 s for 200 lookups at n = 100,000; bubble sort 109 s at n = 60,000; ratios about 4.0 per doubling.

- **Remaining debt:** variance results and Timsort scenario results still pending; noisy 30k-40k rows should be re-run on a quiet machine; entry_id collisions unresolved.

9\. Files in week_09/

|                                                      |                                                        |
|------------------------------------------------------|--------------------------------------------------------|
| **File**                                             | **Purpose**                                            |
| week_09_gate.py                                      | Hardware profile + linear vs. bisect lookup benchmark  |
| BENCHMARK_RESULTS.md, benchmark_output.txt, NOTES.md | Captured run and decisions                             |
| bubble_sort_benchmark.py / bubble_sort_results.json  | Scaling benchmark and raw data                         |
| bubble_sort_report.py, report/index.html             | Charts and HTML report                                 |
| BUBBLE_SORT_RESULTS.md                               | Captured bubble sort output                            |
| variance_study.py                                    | Repeated-trial variance study (running at session end) |
| timsort_vs_bubble.py (planned)                       | Bubble vs. Timsort across three input scenarios        |
