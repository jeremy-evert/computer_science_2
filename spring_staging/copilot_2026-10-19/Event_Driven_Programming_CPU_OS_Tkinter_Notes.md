**From Keypress to Handler**

Event-Driven Programming, CPUs, Operating Systems, Input Devices, and Tkinter State

*A classroom artifact from a conversation with Microsoft Copilot*

Prepared for Jeremy Evert, SWOSU Computer Science

October 19, 2026

*(If the contents list is empty, right-click it in Word and choose Update Field.)*

Part 1: What Does "The Handler Runs" Mean?

> *Question: Event-driven programming: something happens, a handler runs, state changes, the display refreshes. What does "the handler runs" mean, and what does that code look like for a web page or for Tkinter?*

A **handler** is a function you write ahead of time and give to the system. You never call it yourself. You register it, meaning you tell the system "when this happens, run that." Then you hand control to the **event loop**, which waits for something to happen. When the event arrives, the loop calls your function for you. That is what "the handler runs" means.

The flow, step by step

| **Step**              | **What is happening**                        | **Tkinter**                      | **Web page**                        |
|-----------------------|----------------------------------------------|----------------------------------|-------------------------------------|
| 1\. Register          | "When X happens, call this function"         | command=on_click, root.bind(...) | addEventListener(...)               |
| 2\. Hand off          | Your code stops driving; the loop takes over | root.mainloop()                  | The browser does this automatically |
| 3\. Event             | A click, key press or timer tick             | Mouse, keyboard, after()         | Mouse, keyboard, setInterval()      |
| 4\. Handler runs      | The loop calls your function                 | on_click()                       | onClick()                           |
| 5\. State changes     | A variable gets updated                      | cookies += 1                     | cookies += 1                        |
| 6\. Display refreshes | The screen shows the new state               | label.config(...)                | textContent = ...                   |

Both examples below build the same cookie counter so students can compare them line for line. Each has a button handler, a key handler, and a timer handler.

Tkinter version

Paste into PowerShell. It creates cookie_tk.py in the current folder (overwriting any old copy) and runs it.

**PowerShell**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>$code = @'</p>
<p>import tkinter as tk</p>
<p># ---- STATE ----</p>
<p>cookies = 0</p>
<p># ---- DISPLAY ----</p>
<p>def refresh():</p>
<p>label.config(text=f"Cookies: {cookies}")</p>
<p># ---- HANDLERS (we never call these ourselves) ----</p>
<p>def on_click():</p>
<p>global cookies</p>
<p>cookies += 1</p>
<p>print("handler ran: on_click")</p>
<p>refresh()</p>
<p>def on_key(event):</p>
<p>global cookies</p>
<p>if event.char == "r":</p>
<p>cookies = 0</p>
<p>print("handler ran: on_key (reset)")</p>
<p>refresh()</p>
<p>def on_tick():</p>
<p>global cookies</p>
<p>cookies += 1</p>
<p>print("handler ran: on_tick")</p>
<p>refresh()</p>
<p>root.after(3000, on_tick) # re-register for the next tick</p>
<p># ---- BUILD THE WINDOW ----</p>
<p>root = tk.Tk()</p>
<p>root.title("Event-Driven Cookie Counter")</p>
<p>label = tk.Label(root, font=("Arial", 24))</p>
<p>label.pack(padx=20, pady=10)</p>
<p>tk.Button(root, text="Bake a cookie", command=on_click).pack(pady=10)</p>
<p>tk.Label(root, text="Press r to reset. +1 cookie every 3 seconds.").pack(pady=5)</p>
<p># ---- REGISTER HANDLERS ----</p>
<p>root.bind("&lt;Key&gt;", on_key)</p>
<p>root.after(3000, on_tick)</p>
<p>refresh()</p>
<p>print("Setup done. Handing control to the event loop...")</p>
<p>root.mainloop()</p>
<p>print("Window closed. Event loop ended.")</p>
<p>'@</p>
<p>[System.IO.File]::WriteAllText("$PWD\cookie_tk.py", $code, (New-Object System.Text.UTF8Encoding $false))</p>
<p>python .\cookie_tk.py</p></td>
</tr>
</tbody>
</table>

Web page version

This creates cookie_web.html and opens it in the browser. Press **F12** and open the **Console** tab to watch the handler messages.

**PowerShell**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>$html = @'</p>
<p>&lt;!DOCTYPE html&gt;</p>
<p>&lt;html&gt;</p>
<p>&lt;head&gt;&lt;meta charset="utf-8"&gt;&lt;title&gt;Event-Driven Cookie Counter&lt;/title&gt;&lt;/head&gt;</p>
<p>&lt;body style="font-family: Arial; text-align: center;"&gt;</p>
<p>&lt;h1 id="display"&gt;Cookies: 0&lt;/h1&gt;</p>
<p>&lt;button id="bake"&gt;Bake a cookie&lt;/button&gt;</p>
<p>&lt;p&gt;Press r to reset. +1 cookie every 3 seconds.&lt;/p&gt;</p>
<p>&lt;script&gt;</p>
<p>// ---- STATE ----</p>
<p>let cookies = 0;</p>
<p>// ---- DISPLAY ----</p>
<p>const display = document.getElementById("display");</p>
<p>function refresh() { display.textContent = `Cookies: ${cookies}`; }</p>
<p>// ---- HANDLERS (we never call these ourselves) ----</p>
<p>function onClick() {</p>
<p>cookies += 1;</p>
<p>console.log("handler ran: onClick");</p>
<p>refresh();</p>
<p>}</p>
<p>function onKey(event) {</p>
<p>if (event.key === "r") {</p>
<p>cookies = 0;</p>
<p>console.log("handler ran: onKey (reset)");</p>
<p>refresh();</p>
<p>}</p>
<p>}</p>
<p>function onTick() {</p>
<p>cookies += 1;</p>
<p>console.log("handler ran: onTick");</p>
<p>refresh();</p>
<p>}</p>
<p>// ---- REGISTER HANDLERS ----</p>
<p>document.getElementById("bake").addEventListener("click", onClick);</p>
<p>document.addEventListener("keydown", onKey);</p>
<p>setInterval(onTick, 3000);</p>
<p>refresh();</p>
<p>console.log("Setup done. The browser's event loop takes it from here.");</p>
<p>&lt;/script&gt;</p>
<p>&lt;/body&gt;</p>
<p>&lt;/html&gt;</p>
<p>'@</p>
<p>[System.IO.File]::WriteAllText("$PWD\cookie_web.html", $html, (New-Object System.Text.UTF8Encoding $false))</p>
<p>Start-Process .\cookie_web.html</p></td>
</tr>
</tbody>
</table>

Predict and test

- **The classic bug:** change command=on_click to command=on_click(). With the parentheses, Python calls the function once while building the window and gives the button None. One cookie appears at startup, then the button does nothing. Registering a function means passing its name without parentheses.

- **The message after \`mainloop()\`:** "Window closed" only prints after you close the window. The event loop has control the whole time the program runs.

- **Different handler signatures:** in Tkinter, on_key(event) receives an event object but on_click() does not. The system decides what it passes to your handler, not you.

A web server works the same way. In Flask, @app.route("/hello") registers a handler, and the server runs it each time a browser asks for /hello.

Part 2: How a CPU and an Operating System Work

> *Question: How does a CPU and an operating system work? Is a keyboard actually a file on the computer? How does the mouse work?*

A CPU runs one tiny instruction after another, very fast. The operating system is the program that owns the hardware and shares it among all your other programs. A keyboard is not really a file, but on Linux it shows up as one: you can open it and read bytes from it. A mouse never knows where your cursor is. It only reports how far it moved, and the OS does the rest.

The CPU: fetch, decode, execute

1.  **Fetch** the next instruction from memory. A register called the program counter holds its address.

2.  **Decode** it to figure out what it says, such as "add these two registers" or "jump to address 4000."

3.  **Execute** it, move the program counter forward, and start again.

There is no "understanding" anywhere, just a very fast loop over very simple steps like add, compare, load, store and jump. Python’s cookies += 1 becomes a handful of those steps.

The CPU also has a doorbell called an **interrupt**. When hardware needs attention, it signals the CPU. The CPU pauses, saves its place, jumps to an **interrupt handler** the OS registered ahead of time, and then goes back to what it was doing. **That is event-driven programming built into the hardware.** Tkinter handlers are the same idea, many layers higher up.

The operating system: landlord of the hardware

| **Job**          | **What it means**                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Scheduling**   | Gives each program a few milliseconds on the CPU, then switches. It happens so fast that everything seems to run at once. |
| **Memory**       | Gives each program its own private memory space so one program cannot overwrite another.                                  |
| **Drivers**      | Small pieces of code that know how to talk to specific hardware, like a USB keyboard or a graphics card.                  |
| **System calls** | The official way a program asks the OS for help, like "open this file" or "read 3 bytes."                                 |
| **Interrupts**   | The OS owns the doorbell and decides who gets each event.                                                                 |

A timer interrupt fires many times per second. It is how the OS takes the CPU back from a program that would otherwise never let go: the hardware version of root.after().

Is a keyboard a file?

**On Linux and macOS, sort of.** Unix follows the idea that "everything is a file." Devices appear under /dev, and you use the same open() and read() calls you use on a text file. The keyboard is something like /dev/input/event3. Reading it gives small binary records meaning "key 30 went down at time T," not letters. It is not a file on disk; it is a door into a driver.

**On Windows, no.** Devices are kernel objects (for example \Device\KeyboardClass0) that programs reach through handles and Windows APIs, not file paths.

The journey from a key press to your handler

1.  A small chip inside the keyboard constantly scans a grid of switches under the keys.

2.  Pressing **r** makes the chip send a **scan code** (a number for the key’s position, not a letter) over USB.

3.  The USB controller checks the keyboard every few milliseconds, receives the report, and **interrupts the CPU**.

4.  The keyboard **driver** turns the scan code into a key code, using the keyboard layout to decide which letter it is.

5.  The OS queues a key event and sends it to the **window that has focus**.

6.  The program’s event loop takes the event from the queue and **calls \`on_key(event)\`**.

How the mouse works

A modern optical mouse is basically **a tiny camera pointed at the desk**:

1.  An LED or laser lights up the surface.

2.  An image sensor takes thousands of low-resolution pictures per second.

3.  A chip compares each picture with the previous one to work out **dx, dy**: "I moved 4 right and 2 up."

4.  The mouse sends those **relative** numbers plus button states over USB, using the same interrupt path as the keyboard.

5.  The OS adds dx and dy to the cursor position, applies acceleration, and stops the cursor at the screen edges.

6.  The OS finds **which window is under the cursor** and sends it a mouse event, which ends up calling your handler.

**Predict:** pick the mouse up, move it left, and put it down. Does the cursor jump? No. The mouse only reports motion; the cursor’s position exists only inside the OS.

Seeing it for yourself

**Windows (PowerShell):** list the keyboard and mouse devices the OS knows about.

**PowerShell**

|                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------|
| Get-PnpDevice -Class Keyboard,Mouse \| Where-Object Status -eq OK \| Format-Table Class, FriendlyName, InstanceId -AutoSize |

**Linux (Ubuntu on real hardware, not WSL):** read the mouse "file" directly. WSL does not pass real input devices through. Move the mouse to see raw output; press Ctrl+C to stop.

**Bash**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>cat &gt; ~/mouse_peek.py &lt;&lt; 'EOF'</p>
<p>import struct</p>
<p># /dev/input/mice sends 3-byte packets: buttons, dx, dy</p>
<p>with open("/dev/input/mice", "rb") as f:</p>
<p>while True:</p>
<p>buttons, dx, dy = struct.unpack("Bbb", f.read(3))</p>
<p>left = buttons &amp; 1</p>
<p>right = (buttons &gt;&gt; 1) &amp; 1</p>
<p>middle = (buttons &gt;&gt; 2) &amp; 1</p>
<p>print(f"left={left} right={right} middle={middle} dx={dx:+4d} dy={dy:+4d}")</p>
<p>EOF</p>
<p>chmod 755 ~/mouse_peek.py</p>
<p>ls -l /dev/input/</p>
<p>sudo python3 ~/mouse_peek.py</p></td>
</tr>
</tbody>
</table>

Students see that the "mouse file" is a stream of three numbers (buttons, dx, dy), read with the same open() and read() used for text files. The sudo requirement shows the OS guarding hardware; otherwise any program could secretly record keystrokes.

Part 3: Clock Speed and Operations per Second

> *Question: What is a typical clock frequency for a modern desktop, and how many operations per second does it run?*

A modern desktop CPU typically runs at about **3 to 5.5 GHz** (3 to 5.5 billion clock ticks per second), with the fastest chips briefly boosting to around 6 GHz. One tick does not mean one operation, though. A modern desktop can do **hundreds of billions of simple operations per second**, and **trillions** of math operations when it uses vector hardware.

Why it is more than one operation per tick

| **Multiplier**                  | **What it means**                                                                                      | **Typical desktop**            |
|---------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------|
| **Clock speed**                 | Ticks per second                                                                                       | ~5 billion (5 GHz)             |
| **Instructions per tick (IPC)** | Each core has several execution units and runs multiple instructions at once (superscalar, pipelining) | ~3–6 in real code              |
| **Cores**                       | Several full CPUs on one chip                                                                          | 8–24                           |
| **SIMD / vector**               | One instruction works on a whole row of numbers (AVX: 8–16 at once)                                    | ×8 or more for math-heavy code |

A back-of-the-envelope estimate

For an 8-core chip at 5 GHz averaging 4 instructions per tick:

5 × 10⁹ ticks/s × 4 instr/tick × 8 cores = 1.6 × 10¹¹ instr/s

That is about **160 billion instructions per second**. Add vector math, where each instruction handles 8 or more numbers, and you reach **trillions of floating-point operations per second (TFLOPS)**.

The fine print for students

- **Peak is not typical.** Most of the time the CPU waits on memory. A trip to RAM takes around 100 ns, which is hundreds of ticks doing nothing. That is why caches exist.

- **The cookie counter barely uses it.** The CPU spends almost all its time idle, waiting for an interrupt. That is the event-driven picture again.

- **Python is slow by comparison.** One line like cookies += 1 becomes dozens to hundreds of machine instructions, so pure Python runs roughly 10 to 100 million simple operations per second.

Predict, then measure

Ask students to guess how many loop iterations Python can do in one second, then run:

**PowerShell**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>python -c "import time; n=0; t=time.perf_counter(); end=t+1</p>
<p>while time.perf_counter()&lt;end:</p>
<p>for _ in range(100000): n+=1</p>
<p>print(f'Python did about {n:,} additions in 1 second')"</p></td>
</tr>
</tbody>
</table>

Tens of millions versus the hardware’s roughly 160 billion is a natural lead-in to compiled languages, interpreters, and why NumPy exists.

Part 4: A Model, StringVars, and Self-Refreshing Labels

> *Question: What is this code doing, and why does it need to be written like this?*

**The snippet under discussion**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p># ---- OBJECTS ----</p>
<p>model = Inventory() # ONE model object holds the count for BOTH items</p>
<p>root = tk.Tk() # the window</p>
<p>rope_text = tk.StringVar(value="Rope: 0") # text the rope label watches</p>
<p>shovel_text = tk.StringVar(value="Shovel: 0") # text the shovel label watches</p>
<p>total_text = tk.StringVar(value="Total: 0") # text the total label watches</p>
<p># ---- WIDGETS ----</p>
<p>tk.Label(root, textvariable=rope_text).pack()</p>
<p>tk.Label(root, textvariable=shovel_text).pack()</p>
<p>tk.Label(root, textvariable=total_text).pack()</p></td>
</tr>
</tbody>
</table>

This code sets up the **pieces** of a small event-driven app, but nothing happens yet. It creates one object that holds the data, one window, and three labels. Each label watches a StringVar "sticky note," so when the program writes new text on a note, its label updates on screen by itself. There is no handler in this snippet; that comes next.

Line by line

| **Line**                               | **What it does**                                                                   |
|----------------------------------------|------------------------------------------------------------------------------------|
| model = Inventory()                    | Creates the **state**: one object that owns the rope count and the shovel count.   |
| root = tk.Tk()                         | Creates the window and starts Tkinter’s engine underneath.                         |
| rope_text = tk.StringVar(...)          | Creates a Tkinter text holder that widgets can watch.                              |
| tk.Label(root, textvariable=rope_text) | Creates a label that \*watches\* rope_text instead of showing fixed text.          |
| .pack()                                | Places the label in the window. Without it, the label exists but is never visible. |

Why it is written this way

1.  **One model means one source of truth.** Rope, shovel and total all come from the same Inventory object. Since the total is calculated from the model, it cannot drift out of sync.

2.  **The model does not know about Tkinter.** Inventory only does inventory math, so it can be tested with assert without opening a window and reused later with a web page. This is "state changes → display refreshes" written as code.

3.  **\`StringVar\` means the labels refresh themselves.** Instead of label.config(text=...), a handler calls rope_text.set("Rope: 3") and every widget watching that variable redraws. This is the **observer pattern**.

4.  **The order matters.** The StringVar objects must be created \*after\* tk.Tk(), because they attach to the engine Tk() starts. Creating them first raises an error.

5.  **The labels are not stored in variables, on purpose.** The StringVar objects do the updating, so .pack() can go on the same line. Beware: label = tk.Label(...).pack() stores None, because .pack() returns None.

The complete program

This Inventory class is one possible version; the class version may differ. The block creates inventory_tk.py in the current folder (replacing any old copy) and runs it.

**PowerShell**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>$code = @'</p>
<p>import tkinter as tk</p>
<p># ---- MODEL (no tkinter in here) ----</p>
<p>class Inventory:</p>
<p>def __init__(self):</p>
<p>self.counts = {"rope": 0, "shovel": 0}</p>
<p>def add(self, item):</p>
<p>self.counts[item] += 1</p>
<p>def total(self):</p>
<p>return sum(self.counts.values())</p>
<p># ---- OBJECTS ----</p>
<p>model = Inventory() # ONE model object holds the count for BOTH items</p>
<p>root = tk.Tk() # the window (must exist before any StringVar)</p>
<p>rope_text = tk.StringVar(value="Rope: 0") # text the rope label watches</p>
<p>shovel_text = tk.StringVar(value="Shovel: 0") # text the shovel label watches</p>
<p>total_text = tk.StringVar(value="Total: 0") # text the total label watches</p>
<p># ---- DISPLAY: copy model state onto the sticky notes ----</p>
<p>def refresh():</p>
<p>rope_text.set(f"Rope: {model.counts['rope']}")</p>
<p>shovel_text.set(f"Shovel: {model.counts['shovel']}")</p>
<p>total_text.set(f"Total: {model.total()}")</p>
<p># ---- HANDLERS: event -&gt; change model -&gt; refresh ----</p>
<p>def add_rope():</p>
<p>model.add("rope")</p>
<p>print("handler ran: add_rope")</p>
<p>refresh()</p>
<p>def add_shovel():</p>
<p>model.add("shovel")</p>
<p>print("handler ran: add_shovel")</p>
<p>refresh()</p>
<p># ---- WIDGETS ----</p>
<p>root.title("Frontier General Store")</p>
<p>tk.Label(root, textvariable=rope_text, font=("Arial", 16)).pack()</p>
<p>tk.Label(root, textvariable=shovel_text, font=("Arial", 16)).pack()</p>
<p>tk.Label(root, textvariable=total_text, font=("Arial", 16, "bold")).pack()</p>
<p>tk.Button(root, text="Add rope", command=add_rope).pack(pady=4)</p>
<p>tk.Button(root, text="Add shovel", command=add_shovel).pack(pady=4)</p>
<p>refresh()</p>
<p>root.mainloop()</p>
<p>'@</p>
<p>[System.IO.File]::WriteAllText("$PWD\inventory_tk.py", $code, (New-Object System.Text.UTF8Encoding $false))</p>
<p>python .\inventory_tk.py</p></td>
</tr>
</tbody>
</table>

The flow: **click → handler → \`model.add()\` → \`refresh()\` → \`.set()\` → the labels redraw themselves.**

Predict, then break it

- **Move the \`StringVar\` lines above \`root = tk.Tk()\`.** It crashes before the window opens.

- **Write \`x = tk.Label(...).pack()\`, then \`print(x)\`.** It prints None.

- **Delete the \`refresh()\` call in \`add_rope()\`.** The model still counts (the print output proves it), but the screen stays stale. State and display really are separate.

One-Page Summary: The Big Idea

Every layer of the computer uses the same pattern: **register a handler, wait, an event arrives, the handler runs, state changes, the display refreshes.**

| **Layer**        | **The event**                               | **The handler**           | **The state that changes**            |
|------------------|---------------------------------------------|---------------------------|---------------------------------------|
| Hardware         | Key switch closes, mouse moves, timer fires | OS interrupt handler      | Event queue, cursor position          |
| Operating system | Interrupt from a device                     | Driver code               | Event delivered to the focused window |
| Tkinter          | Button click, key, after() tick             | on_click, on_key, on_tick | cookies, model.counts                 |
| Web page         | Click, keydown, setInterval                 | onClick, onKey, onTick    | cookies                               |
| Web server       | HTTP request for /hello                     | Flask route function      | Response sent to the browser          |

Key vocabulary

- **Handler:** a function you register for the system to call when an event happens.

- **Event loop:** the code that waits for events and calls handlers (mainloop(), the browser).

- **Interrupt:** the hardware doorbell that makes the CPU pause and run an OS handler.

- **Kernel / driver / system call:** the OS core, its hardware translators, and the official request door.

- **Clock speed vs. throughput:** GHz counts ticks; IPC, cores and SIMD multiply real work.

- **Model / view separation:** keep data logic out of the GUI so it can be tested and reused.

- **Observer pattern:** widgets watch a StringVar and redraw themselves when it changes.
