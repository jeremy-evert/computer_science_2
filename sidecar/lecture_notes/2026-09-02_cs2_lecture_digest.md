# CS2 lecture digest — Wednesday, September 2, 2026

## Evidence and privacy

- Course: Computer Science II (COMSC-1053), Fall 2026.
- Source: fresh local Whisper/CTranslate2 transcription of the protected MP4.
- Protected MP4: `Fall 2026 Computer Science II (COMSC-1053-1417)-20260902_130052-Meeting Recording.mp4`.
- Fresh transcript: same base name, `.vtt`, in the protected input directory on April.
- This was an open-lab/pairing session, not a lecture from the front of the room: the instructor circulated between small groups. The digest omits student names, pairing assignments, chat, and any identifying classroom detail; groups are referred to only by role (Foreman/Worker/Navigator).

## Session shape

Unlike Monday's structured lecture, Wednesday was a hands-on lab session built around Monday's "Found Your World" material. The instructor opened with a short aside about an unrelated GPU benchmarking experiment (comparing a 2080 Super, a 5080, and several 30/40/50-series cards, and a Linux-vs-Windows-native question) — noted here as instructor research context, not course content — then handed off into the day's actual task.

## Teaching goals

1. Get every pair to actually run a local model, not just talk about running one.
2. Reuse the Foreman/Worker (and, for larger groups, Navigator) pairing structure so one student drives the keyboard while the other documents and questions.
3. Anchor the exercise in Monday's four World Bible scenarios (Frontier Settlement, Investigation Bureau, Starship Log, Small Business) as a lightweight narrative frame for testing a model.
4. Introduce variance and load-time as concrete, measurable properties of a model response — not just "did it work."
5. Model the workflow of asking Copilot/ChatGPT for a rough script, reading it, and iterating — rather than either hand-writing everything or trusting the output unread.
6. Reward durable evidence: bonus points for pushing artifacts to GitHub and keeping lab notes.

## Concepts actually covered

### Continuity with Monday

The instructor pointed students back to the archived Monday recording and its slide deck (both already linked in the module) as the reference material to work alongside during today's lab, specifically the section on the World Bible and how it fits into a model prompt.

### Pairing roles

Pairs were assigned Foreman/Worker roles (with one three-person group also using a Navigator), rotating who drives the keyboard. The instructor's guidance for the Foreman role: get the Worker to narrate intent in a document before acting ("I'm going to hit this website, then do this step"), and to intervene when the Worker notices something interesting on screen but doesn't stop to ask about it — that noticing-and-not-following-up moment is exactly what should get escalated to Copilot/ChatGPT for explanation.

### Picking a world and getting a model talking

Students chose one of the four "Answer a call" World Bible scenarios (each a one-line premise with a built-in inconsistency: a mismatched grain count, a mismatched records timestamp, a sensor behaving strangely, a mismatched inventory count) and used it as the seed for a Copilot/ChatGPT prompt, then carried that prompt over to a locally running model. The instructor's own worked example: an "Investigation Bureau" prompt, sent to Copilot, that came back with a PowerShell script scaffold — `Start-Transcript` to log the session, `Get-CimInstance` calls for OS/CPU inventory, and an `nvidia-smi` section — which the instructor then read, thought aloud about, and started pasting into a real terminal rather than accepting it uninspected.

### Reading real machine evidence

The instructor ran `nvidia-smi` live to show what a real GPU status readout looks like: an RTX 3060 Ti with roughly 2.3 GB of its 8 GB VRAM already in use at idle by ordinary background processes (browser, Teams, shell). This was tied back to the opening aside — VRAM headroom, not raw GPU tier, is often the practical ceiling on which models fit.

### Variance and load time as a measurement, not a vibe

The instructor used a repeated "knock knock" call-and-response with a student as a live analogy for model variance: asking the same model the same question multiple times and getting inconsistent replies is the same kind of "wiggle" you'd see if a person mangled a knock-knock joke's expected response. From there: ask a model the same question five times and describe the variance; ask it the same question three times and describe the time variance; distinguish a model's cold load (first invocation, paying to bring weights into VRAM) from a hot load (already resident). This was explicitly tied forward to the course's later Computer Architecture material on memory.

### A practical pipelining tip

For students downloading a second, larger model while still experimenting with a small one already running: open a second PowerShell window and start the `ollama pull` there. A model pull is mostly network and disk I/O, not GPU-bound, so it does not meaningfully compete with a model already running in the first window.

### Bonus structure for the Foreman role

Two explicit bonus criteria were given to whoever was in the Foreman role: (1) get durable artifacts — the Worker's outputs — pushed into GitHub, especially valuable if the Worker was new to GitHub; (2) get things written into documents/lab notes, framed as building the habit of a working scientist keeping a record, not just producing a final answer.

## Useful examples and timestamps

| Approx. time | Evidence / teaching move |
|---|---|
| 00:00–01:52 | Instructor aside: unrelated GPU benchmarking experiment (2080 Super/5080/30-50 series, Linux vs. Windows native) — context, not course content |
| 04:02–04:49 | Pointing students to Copilot sign-in and the archived Monday recording + slides |
| 06:29–06:44 | Pointing to the Hardware Confidence slide deck as a starting reference |
| 06:49–09:53 | Assigning Foreman/Worker/Navigator pairs and roles for the session |
| 09:53–10:37 | Choosing one of the four World Bible scenarios as the day's task |
| 11:09–11:29 | `nvidia-smi` shown as the "Foreman" tool for reading GPU state |
| 11:34–13:41 | Worked example: prompting Copilot with "I am on a computer, I want to test how different models reply," then an Investigation Bureau world seed |
| 14:05–14:25 | Naming the mental model explicitly: local prompt to a web UI is a request sent to someone else's computer |
| 15:07–16:12 | Reading and pasting the Copilot-generated PowerShell scaffold (`Start-Transcript`, `Get-CimInstance`, `nvidia-smi`) into a real terminal, uploading a generated session-transcript file back into the chat for context |
| 16:40–17:29 | The "knock knock" bit as a live variance analogy |
| 17:29–18:22 | Framing variance and cold-load-vs-hot-load timing as the measurable target for the day, tied forward to Computer Architecture |
| 18:52–19:17 | Bonus-point criteria for the Foreman role: GitHub artifacts and lab notes |
| 19:17–20:15 | Circulating to check in with pairs; troubleshooting a stalled Ollama model download live |
| 21:16–21:52 | Two-terminal-window tip: run one model while pre-pulling a second in a separate window |

## Corrections and follow-up notes

- **LECTURE SAID:** "It's not necessarily for [the Worker] to do whatever the assignment is... it's more like, what do you think would be cool for you to go figure out."
  **FOLLOW-UP NOTE:** worth stating explicitly in the published notes that today's session was intentionally open-ended and exploratory rather than a fixed rubric task — the fixed "Which Model Would You Hire?" discussion/assignment is the separate, already-published Week 3 item due the same day.
- **LECTURE SAID:** a pull "doesn't actually interfere with your GPU most of the time."
  **FOLLOW-UP NOTE:** true for the download itself; a pulled model that finishes and gets loaded while another is still resident is the scenario that can actually compete for VRAM — worth a one-line caveat if this tip is repeated.

## Unfinished threads and next steps

- No explicit "next class" preview was stated in this session; the standing due date already on the module (Week 3 — Which Model Would You Hire?, due Sept. 2) remains the natural checkpoint.
- Consider publishing a short version of the nvidia-smi / Start-Transcript / Get-CimInstance script pattern as a reusable Week 3 handout, since it came out of a live improvised Copilot prompt rather than a prepared resource.
