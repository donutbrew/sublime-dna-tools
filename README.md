# DNA Tools for Sublime Text

A lightweight Sublime Text 3/4 plugin for manipulating DNA sequences directly in the editor. Includes support for IUPAC ambiguity codes.

Somehow it seems this doesn't yet exist, and I frequently wish it did. So here we are. If there are more tools I need, I'll add them.

---

## Features

-  **Reverse Complement**: Reverses and complements selected DNA sequences
-  **Complement Only**: Applies IUPAC complement rules without reversing
-  **Reverse Only**: Simply reverses the selected text

Supports both uppercase and lowercase bases, including ambiguous bases like `R`, `Y`, `W`, `S`, `N`, etc.

---

## IUPAC Complement Rules

| Base | Complement |
|------|------------|
| A    | T          |
| T    | A          |
| C    | G          |
| G    | C          |
| R    | Y          |
| Y    | R          |
| S    | S          |
| W    | W          |
| K    | M          |
| M    | K          |
| B    | V          |
| D    | H          |
| H    | D          |
| V    | B          |
| N    | N          |

---

## Installation

### Manual Install

1. Open `Preferences → Browse Packages…`
2. Clone this repo into the `User/` directory:
   ```bash
   git clone https://github.com/donutbrew/sublime-dna-tools.git "DNA Tools"


---

## Usage

Highlight any DNA sequence in your Sublime editor, then:

### Command Palette

Press `Ctrl+Shift+P` / `Cmd+Shift+P` and type:

- `DNA Tools: Reverse Complement`
- `DNA Tools: Complement Only`
- `DNA Tools: Reverse Only`

### Optional Keybindings

To bind to hotkeys, open `Preferences > Key Bindings` and add:

```json
[
  { "keys": ["ctrl+alt+r"], "command": "reverse_complement" },
  { "keys": ["ctrl+alt+c"], "command": "complement_only" },
  { "keys": ["ctrl+alt+e"], "command": "reverse_only" }
]
