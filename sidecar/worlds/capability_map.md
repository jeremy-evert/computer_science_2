# CS2 Capability-to-World Opportunity Map

Internal canon. Maps the existing CS2 technical spine
(`../../assignments/A2-coding-odyssey-project.md`'s growth path) to
opportunities in each of the four worlds. This does not rewrite the
curriculum -- it is a reference for authoring authentic, world-native
problems without duplicating a single technical concept four times in
four unrelated ways.

Weeks and capability codes (S01, S02, ...) match
`../../assignments/A2-coding-odyssey-project.md` and
`../../planning/fall-2026-course-design.md` exactly. If either source
changes, update this map rather than letting it drift.

| Weeks | Capability | Frontier Settlement | Investigation Bureau | Starship Log | Small Business |
|---|---|---|---|---|---|
| 3-4 | S01 sound collaborating objects, composition, invariants | A household's water allocation must never go negative or double-claim a well slot | An evidence item can never be checked out by two people at once | Life-support readings must never contradict known physical limits | Inventory count must never go negative; orders must never ship unpaid |
| 5 | S02 earned inheritance/polymorphism | Claim types (homestead, mill, trade-post) sharing a common Claim contract | Case types (property, missing-persons, fraud) sharing a common Case contract | Sensor types (thermal, spectral, proximity) sharing a common Sensor contract | Product types (hardware, seasonal, special-order) sharing a common Product contract |
| 6 | S03 contracts (checkpoint) | Two merging settlements' incompatible ledger formats | Two agencies' field-report formats that don't match | Two subsystems built to different eras' interface standards | A new supplier's data format that doesn't match the existing system |
| 7-8 | S05/S06 data abstractions, list/stack/queue, search/order tradeoffs | Prioritizing well-drilling requests; sorting the mill queue | Sorting evidence by custody order vs. relevance; case backlog | Triaging sensor alerts by severity vs. arrival | Prioritizing supplier orders by urgency vs. cost |
| 9 | S04 compact GUI/events (checkpoint) | Public notice board: well allocations, mill queue | Case-status dashboard for field investigators | Bridge status console summarizing subsystem health | Daily register/inventory screen Frank can read at the counter |
| 10 | S09 honest data visualization | Population growth vs. water supply | Case backlog and closure-rate trend | Resource (fuel/power/life-support) consumption trend | Margin-per-product honesty chart |
| 11 | S09 storytelling / flex | Evidence-backed claim about settlement growth capacity | Evidence-backed claim about case-handling capacity | Evidence-backed claim about mission resource margins | Evidence-backed claim about business sustainability |
| 12-13 | S08 synthesis, stabilization, culmination | Reconciling Merrow's and Old Tobin's conflicting ledgers | Reconciling two versions of a case file after review | Reconciling two subsystem logs after a diagnostic disagreement | Reconciling two versions of the inventory count |
| 14 | S08 workflow/reproducibility (checkpoint) | Recorder's Office history/recovery receipt | Case Records Division history/recovery receipt | Ship's Log history/recovery receipt | Back-office history/recovery receipt |
| 16 | shared Farkle/ML (not an Odyssey gate) | *not world-specific -- shared experience, see A2 "Week 16-17"* | | | |

## How to use this

When authoring a new week's world-specific example, gate flavor text,
or injection: find the week's capability row, then write the specific
scenario for the target world fresh -- do not just re-word the table
cell. The table cell is a starting spark, not finished prose. The goal
stated in Prompt 017 stands: the same capability should surface
*differently*, not as noun substitution -- if two worlds' scenarios for
the same week feel interchangeable after drafting, revise one.

Every scenario above must still be satisfiable by multiple legitimate
student designs. Never let a world scenario secretly imply one correct
object model -- see `README.md`'s "World Bible vs. the student's World
Bible" section.
