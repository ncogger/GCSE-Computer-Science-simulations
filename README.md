# GCSE Computer Science simulations

Interactive simulations for the Pearson Edexcel GCSE (9–1) Computer Science specification (1CP2).

Each simulation is a single self-contained HTML file with no external dependencies, so it works offline, on a school network, or uploaded to Moodle as a File resource (Display: Open or New window).

| File | Topic | Spec |
|---|---|---|
| `fde-cycle.html` | Fetch–decode–execute cycle, buses, registers, stored program concept, Z80 pinout | 3.1.1 |
| `binary-register.html` | Binary ↔ denary, two's complement, binary addition and overflow, logical and arithmetic shifts | 2.1.1–2.1.5 |
| `sort-search.html` | Bubble sort, merge sort, linear search, binary search, efficiency comparisons | 1.2.6–1.2.7 |
| `trace-table.html` | Trace tables for Python programs, fill-it-in practice, finding syntax, runtime and logic errors | 1.2.1, 1.2.4–1.2.5 |
| `tcp-ip.html` | A message's journey through the 4-layer TCP/IP model: packets, headers, IP addresses, routers, lost and out-of-order packets, HTTP/HTTPS/SMTP/IMAP/POP3/FTP | 4.1.3, 4.1.6–4.1.7 |
| `sound-sampling.html` | Sampling an analogue sound wave: sample rate, sample interval, bit depth, amplitude levels, playback of the digitised sound, file-size calculations | 2.2.3–2.2.4, 2.3.1 |
| `bitmap-builder.html` | Pixel editor with each pixel's binary code, colour depth and palettes, decode-the-binary challenges, resolution and colour depth effects on a picture, file-size calculations | 2.2.2, 2.2.4, 2.3.1 |
| `logic-gates.html` | AND, OR and NOT: live circuits drawn from any expression with up to three inputs, truth tables with working columns, complete-the-table challenges, real-life problems | 1.3.1 |

## BTEC National Computing – Unit 2: Computer Network Security and Encryption

Simulations for the Pearson BTEC National in Computing (2025), Unit 2, are in the `btec-unit2/` folder. Algorithms are shown as numbered plain-English instructions, the style the mark schemes credit, and challenges use the specification's command words (Describe, Explain, Evaluate, Develop, Complete).

| File | Topic | Spec |
|---|---|---|
| `btec-unit2/cipher-lab.html` | Substitution (Caesar and keyword), transposition (rail fence and columnar), XOR, one-time pad (and what goes wrong if a pad is reused), Enigma-style rotor cipher, LSB steganography; step-through algorithms, frequency analysis and brute force, strengths and weaknesses, put-the-algorithm-in-order challenges | C1.5.1 |
| `btec-unit2/attack-defend.html` | Nine network attacks (eavesdropping, interception, replay, ARP spoofing, DNS poisoning, man-in-the-middle, crypto-jacking, SQL injection, buffer overflow) animated step by step on a network, login form, memory or CPU view, each with a defence toggle that shows the countermeasure stopping it; put-the-attack-in-order and choose-the-defence challenges | B1, B2, B3 |

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
