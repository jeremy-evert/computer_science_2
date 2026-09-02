# Sept. 2 lecture notes — running your own model, and measuring it

This was our open-lab day: you and your partner picked one of Monday's World
Bible scenarios and got a local model actually talking back. These notes
distill what came up while circulating between groups, so you have it in
writing even if you were focused on your own screen at the time.

## Foreman / Worker (and Navigator)

Pairs split into a Foreman and a Worker; a few three-person groups added a
Navigator. The Worker drives the keyboard. The Foreman's job is not to take
over -- it's to keep a running narration of intent ("I'm going to open this
page, then do this") and to catch the moments where the Worker notices
something interesting on screen but doesn't stop to ask about it. That
noticing-and-not-following-up moment is exactly the kind of thing worth
pasting into Copilot or ChatGPT and asking about.

## Picking a world

Four scenarios were on the table, each with a built-in inconsistency to
chase down:

- **Frontier Settlement** -- a mill's grain count has started coming up short.
- **Investigation Bureau** -- a records report has a timestamp that doesn't match.
- **Starship Log** -- a sensor has been behaving strangely.
- **Small Business** -- inventory has come up short twice.

Whichever one you picked, the move was the same: turn the one-line premise
into a prompt, hand it to a local model, and see what comes back.

## Asking Copilot for a script, then reading it before you run it

The instructor's own worked example: send Copilot a plain-language ask ("I am
on a computer, I want to test how different models reply, help me see what
works and doesn't work"), get back a PowerShell scaffold, and then actually
read it before pasting it in -- not just trust it. The scaffold that came
back opened a session transcript log (`Start-Transcript`), pulled basic
machine info (`Get-CimInstance`), and included an `nvidia-smi` section for
GPU state. This is a reusable pattern: describe the goal, get a draft, read
every line, then run it.

## Reading `nvidia-smi`

`nvidia-smi` is your quickest way to see what's actually happening on the
GPU: how much VRAM is already in use before you've loaded anything, what
processes are touching it, and how hot/loaded the card is. On the instructor's
own machine, an RTX 3060 Ti already had a couple of gigabytes of its 8 GB
VRAM in use just from ordinary background applications -- worth checking
before you conclude a model "doesn't fit."

## Variance is a real, measurable thing

Ask a model the same question five times in a row and you'll get different
answers -- that's variance, and it's worth describing, not just noticing.
Ask it the same question three times and time each response -- you'll see
the difference between a **cold load** (the model's weights are being pulled
into VRAM for the first time) and a **hot load** (it's already resident and
answers faster). This connects directly to the memory/architecture
conversation we'll pick back up later in the course.

## A pipelining tip

If you're waiting on a big model to download while you're still experimenting
with a smaller one that's already running, open a second PowerShell window
and start the `ollama pull` there instead of waiting. A model download is
mostly network and disk, not GPU -- so it won't meaningfully slow down the
model you already have running.

## Foreman bonus points

Two things earn bonus credit if you were in the Foreman role today: (1) get
your Worker's output pushed to GitHub as a durable artifact, especially
valuable if they're new to Git; (2) keep it written down -- lab notes are
part of doing science, not an afterthought.

## Where the recording and slides live

Monday's archived lecture recording and slide deck are linked earlier in
this module if you want to revisit the World Bible material this session
built on.
