# Before Map: `beast.py` As It Is

Line references are to the current `beast.py`.

## Diagram A — Who calls whom, and what they share

```mermaid
flowchart LR
    Main["main entry"] -->|calls| Go["go()"]
    Go -->|via fn| Bs["bs(a)"]
    Go -->|via fn| Bs2["bs2(a)"]
    Go -->|via fn| Ins["ins(a)"]
    Go -->|via fn| Sel["sel(a)"]
    Go -->|via fn| PySort["pysort(a)"]
    PySort -->|comparator| Cmp["cmp(x, y)"]
    Go -->|search| Lin["lin(a, x)"]
    Go -->|search| Binr["binr(a, x)"]

    subgraph Shared["shared mutable state"]
        C[("C: comparisons")]
        S[("S: swaps")]
        P[("P: probes")]
        R[("R: sort results")]
    end

    Bs -.->|+=| C
    Bs -.->|+=| S
    Bs2 -.->|+=| C
    Bs2 -.->|+=| S
    Ins -.->|+=| C
    Ins -.->|+=| S
    Sel -.->|+=| C
    Sel -.->|+=| S
    PySort -.->|+=| C
    Cmp -.->|+=| C
    Lin -.->|+=| P
    Binr -.->|+=| P
    Go -.->|reset| C
    Go -.->|reset| S
    Go -.->|reset| P
    Go -.->|=| R

    Go --> Magic["magic numbers"]
    Go --> Latex["string LaTeX"]

    classDef entry fill:#283593,color:#fff,stroke:#1a237e,stroke-width:2px;
    classDef orchestrator fill:#00897b,color:#fff,stroke:#00695c,stroke-width:2px;
    classDef algorithm fill:#e0f2f1,color:#173b36,stroke:#26a69a,stroke-width:1.5px;
    classDef smell fill:#fff0f0,color:#5b1010,stroke:#c62828,stroke-width:2px;
    class Main entry;
    class Go orchestrator;
    class Bs,Bs2,Ins,Sel,PySort,Cmp,Lin,Binr algorithm;
    class C,S,P,R,Magic,Latex smell;
```

### Diagram A smells

- `C`, `S`, `P`, and `R` are shared mutable globals declared at lines 14–17.
- `bs` and `bs2` repeat nested bubble-sort loops, with early exit only in `bs2` (lines 25–53).
- The sizes, trial count, lookup count, and input range are fixed numeric values (lines 18–20, 146, 172, and 178).
- `go()` builds LaTeX by concatenating strings across lines 216–253.

## Diagram B — What `go()` does, in order

```mermaid
flowchart TD
    Start["go starts"] --> Setup["create output folder\nlines 127–130"]
    Setup --> SortSetup["open sorting CSVs\nlines 131–136"]
    SortSetup --> Inputs["build sorted inputs\nlines 137–150"]
    Inputs --> Sort["run sorting trials\nlines 151–160"]
    Sort --> SortWrite["write sorting rows\nlines 161–164"]
    SortWrite --> Search["build and search inputs\nlines 166–187"]
    Search --> SearchWrite["write search rows\nlines 188–189"]
    SearchWrite --> PlotGate["if plotting available\nline 191"]
    PlotGate --> Plots["draw and save plots\nlines 192–214"]
    PlotGate --> Latex["build report strings\nlines 216–253"]
    Plots --> Latex
    Latex --> TexWrite["write report.tex\nlines 254–256"]
    TexWrite --> Compile["run pdflatex\nlines 258–263"]
    Compile --> Done["print completion\nline 264"]

    SortWrite --> SortCsv["out/sort_counts.csv"]
    SortWrite --> TimingCsv["out/timings.csv\nchanges every run"]
    SearchWrite --> SearchCsv["out/search_counts.csv"]
    Plots --> SortPng["out/sort_counts.png"]
    Plots --> SearchPng["out/search_probes.png"]
    TexWrite --> Tex["out/report.tex"]
    Compile --> Pdf["out/report.pdf"]

    Magic["magic numbers"] -.-> Inputs
    Magic -.-> Search
    Latex -.-> TexWrite

    classDef entry fill:#283593,color:#fff,stroke:#1a237e,stroke-width:2px;
    classDef orchestrator fill:#00897b,color:#fff,stroke:#00695c,stroke-width:2px;
    classDef algorithm fill:#e0f2f1,color:#173b36,stroke:#26a69a,stroke-width:1.5px;
    classDef smell fill:#fff0f0,color:#5b1010,stroke:#c62828,stroke-width:2px;
    class Start entry;
    class Setup,SortSetup,Inputs,Sort,SortWrite,Search,SearchWrite,PlotGate,Plots,Latex,TexWrite,Compile,Done orchestrator;
    class SortCsv,TimingCsv,SearchCsv,SortPng,SearchPng,Tex,Pdf algorithm;
    class Magic,Latex smell;
```

### Diagram B smells

- Fixed sizes and counts, plus numeric input-range values, appear at lines 18–20, 146, 172, and 178.
- `go()` assembles the LaTeX document through string concatenation at lines 216–253.

### Unverified

- `pdflatex` is invoked at lines 258–260 with `-output-directory out`; the exact PDF filename and any auxiliary files depend on the installed `pdflatex` behavior. The PDF node represents the expected `out/report.pdf` output, not a verified artifact.
