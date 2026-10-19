# GCSE Computer Science simulations

Interactive simulations for the Pearson Edexcel GCSE (9–1) Computer Science specification (1CP2).

Each simulation is a single self-contained HTML file with no external dependencies, so it works offline, on a school network, or uploaded to Moodle as a File resource (Display: Open or New window).

| File | Topic | Spec |
|---|---|---|
| `fde-cycle.html` | Fetch–decode–execute cycle, buses, registers, stored program concept, Z80 pinout | 3.1.1 |
| `binary-register.html` | Binary ↔ denary, two's complement, binary addition and overflow, logical and arithmetic shifts | 2.1.1–2.1.5 |
| `sort-search.html` | Bubble sort, merge sort, linear search, binary search, efficiency comparisons | 1.2.6–1.2.7 |
| `trace-table.html` | Trace tables for Python programs, fill-it-in practice, finding syntax, runtime and logic errors | 1.2.1, 1.2.4–1.2.5 |

## Features shared by every simulation

- **Revision mode**: an explanation panel with "How it works", "Key ideas" and a "Check yourself" quiz.
- **Presenter mode** (`P`): hides the panel and enlarges everything for a projector, with a one-line caption.
- **Predict / Challenge** (`Q`): asks pupils what will happen before each step, or sets practice questions.
- Keyboard and presentation-clicker control (`Space` / `PgDn` to step, `←` / `PgUp` to go back). Press `?` in any simulation for the full list.

## House style

The simulations follow the Computing department's Classroom Resources Style Guide: Lexend headings, Atkinson Hyperlegible Next body text and Atkinson Hyperlegible Mono code, school navy (#001F5B) with a St David's gold (#85764d) accent line, no italics or capitals blocks, and explanation boxes that match the guide's components (Instruction, Key word, Hint, Challenge) by border and icon.

The fonts are embedded in each file so they work offline. To restyle after editing a simulation, run:

```
python3 tools/apply_house_style.py
```

The fonts are kept in `tools/fonts` (SIL Open Font Licence), so `python3 tools/apply_house_style.py` works with no arguments.

## Adding to Moodle

1. Turn editing on → Add an activity or resource → **File**.
2. Upload the `.html` file.
3. Under Appearance, set Display to **Open** (or **New window** for full screen on a projector).
