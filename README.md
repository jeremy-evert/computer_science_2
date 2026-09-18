# Computer Science 2

COMSC-1053 is a Fall 2026 continuation course organized around a
CS2-specific Reasoning Odyssey: object boundaries, composition and
inheritance, contracts, data abstractions, GUI/event work, data
visualization/storytelling, and professional workflow. The repository is
course-source truth for that progression and its evidence/rubrics.

Start with START_HERE.md, then use [\ROADMAP.md\](ROADMAP.md)
and docs/repo-map.md to understand current ownership.
Grading categories and the Week 4-15 gate/checkpoint shape are in
[\docs/grading-model.md\red Week 1, Week 2, AI Fluency I, and Professional Minds material is
referenced at its owning repository rather than duplicated here. This is a
source-only repository: deployment is a separate authorized step.

---

## 🌐 Live Course Website

The course landing page is published via GitHub Pages:

> **https://jeremy-evert.github.io/computer_science_2/**

- The root \index.html\ redirects to the current semester page (\FA26.html\).
- No login required — anyone with the link can view it.

---

## 🧑‍🎓 Student Contribution Guide

### Step 1 — Visit the Live Site
Open your browser and go to:
\\\
https://jeremy-evert.github.io/computer_science_2/
\\\

### Step 2 — Clone the Repo (first time only)
\\\ash
git clone https://github.com/jeremy-evert/computer_science_2.git
cd computer_science_2
\\\

### Step 3 — Create Your Own Page
Name your file using your SWOSU username, e.g. \smithj.html\.
You can copy the current semester page as a starting point:
\\\ash
cp FA26.html smithj.html
\\\
Then open \smithj.html\ in your editor and make it your own.

### Step 4 — Stage, Commit, and Push Your Page
\\\ash
git add smithj.html
git commit -m "Add smithj personal page"
git push
\\\

### Step 5 — Add a Link to Your Page on the Main Site
Open \FA26.html\ and find the student links section.
Add a line like this:
\\\html
<li>html">Smith, Jordan</a></li>
\\\
Then save, stage, commit, and push:
\\\ash
git add FA26.html
git commit -m "Add smithj link to FA26 class page"
git push
\\\

### Step 6 — See Your Work Live
Wait about 60 seconds, then refresh:
\\\
https://jeremy-evert.github.io/computer_science_2/FA26.html
\\\
Your link will be there. Click it. That is your page on the internet. 🎉

---

## 🔁 Everyday Git Workflow (the short version)

\\\ash
git pull                        # always start here — get the latest
# ...make your changes...
git add <yourfile.html>         # stage what you changed
git commit -m "describe what you did"   # save a snapshot
git push                        # send it to GitHub
\\\

---

## ⚠️ Rules of the Road

- **Always \git pull\ before you start editing.** This prevents merge conflicts.
- **Name your file after your SWOSU username.** No spaces, lowercase only.
- **Do not edit other students' files** without their permission.
- **Commit messages should be human-readable.** Future-you will thank present-you.
- Have fun — this is a real website that real people can visit. Make it good. 🚀
