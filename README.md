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
| `btec-unit2/keys-lab.html` | Symmetric vs asymmetric (who holds which key, what an eavesdropper can do, how many keys a group needs), RSA key generation and encryption with small primes (and why the primes must be huge), real AES-128 stepped round by round with the avalanche effect, the TLS handshake with a genuine or fake certificate; order-the-algorithm, calculation and choose-the-right-encryption scenario challenges | C1.4, C1.5.2, D1 |
| `btec-unit2/hash-lab.html` | Real MD5, SHA-256 and SHA3-256: checking a file's integrity (with tampering), hash properties and the avalanche effect, a genuine MD5 collision; password storage with and without salt and a lookup-table attack; digital signatures (tampered and forged documents); certificates and the PKI chain of trust (valid, expired, wrong domain, self-signed, revoked); order-the-algorithm and exam-style questions | C1.6–C1.9 |
| `btec-unit2/packets-lab.html` | A real TCP/IP frame built and dissected byte by byte (click any field); packet switching with TCP vs UDP handling a lost and an out-of-order packet; one packet followed hop by hop to show which addresses change, with IPv4, IPv6 and MAC explorers; the ten protocols in the spec with ports, TCP/UDP, handshakes and encryption; order-the-algorithm, calculation and exam-style challenges | C1.1–C1.3 |
| `btec-unit2/raid-lab.html` | RAID 0, 1, 5 and 10: watch a file being written across the disks, click any disk to fail it, and see whether the data survives (RAID 5 rebuilds missing blocks with XOR parity, shown in binary); usable-capacity calculator; full, incremental and differential backups over a week with a ransomware restore; why RAID is not a backup | A2.2.4, B3.3.2, B3.4.8 |
| `btec-unit2/firewall-lab.html` | A college firewall: 12 packets checked against an editable rule table (first match wins, default policy), with three deliberate mistakes to fix until every packet follows the security policy; IDS vs IPS with signature, anomaly or both, showing true/false positives and negatives, the zero-day that signatures miss and false alarms an IPS turns into blocked work | B3.1, B3.3.3, B3.3.8–B3.3.9 |
| `btec-unit2/passwords-lab.html` | Password strength (character pool, length, possible passwords and time to guess for a login page, slow and fast hashes; common-password and passphrase handling) and a modern password policy check; multi-factor authentication with a leaked password, MFA on and off; biometric match scores, threshold and FAR/FRR trade-off; access control with least privilege and joiners–movers–leavers | B3.2.2–B3.2.3, B3.4.3 |
| `btec-unit2/network-designer.html` | Design a secure network for a college, a water treatment works, a software company or a factory: seven decisions (boundary/DMZ, segmentation, Wi-Fi, remote access, monitoring, backups, device hardening) redraw the network diagram, tick off the scenario's requirements and score the design on security, performance, usability, scalability and cost against a budget; step through an evaluation of your own design; model designs; network types, topologies and device security settings | A1, A2.3, B3.1, B3.3.7, D2 |
| `btec-unit2/risk-lab.html` | The CIA triad: predict which of confidentiality, integrity and availability eight incidents affect, then see why and a control for each; a college risk register with likelihood × impact scores on a live 5×5 risk matrix, ranking, and reduce/transfer/avoid/accept treatments with residual risk; an incident response plan for ransomware with and without a plan, daily or hourly backups, against RTO and RPO targets | B3.4.1, B3.4.4–B3.4.8, D2.8 |

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
