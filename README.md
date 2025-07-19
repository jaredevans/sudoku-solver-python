# sudoku-solver-python
Recursively solves sudoku puzzles

# Sudoku Solver (Python, CLI)

A simple, interactive command-line Sudoku solver written in Python.  
Enter your own Sudoku puzzle, or use the provided defaults. The solver uses a backtracking algorithm and reports the number of attempts taken to solve the puzzle.

---

## Features

- **User-friendly input**: Enter a custom puzzle line by line, or press Enter to use a default example.
- **Fast backtracking algorithm**: Efficiently solves most valid 9x9 Sudoku puzzles.
- **Attempts counter**: Displays how many placement attempts were made.
- **Readable grid printing**: View both the original and solved grids.

---

## Requirements

- Python 3.9 or newer (type hints use modern syntax)
- No third-party libraries required

---

## Usage

1. **Clone this repository:**
    ```bash
    git clone https://github.com/jaredevans/sudoku-solver-python.git
    cd sudoku-solver-python
    ```

2. **Run the solver:**
    ```bash
    python sudoku.py
    ```

3. **Follow the prompts:**  
   Enter each row (9 digits, 0 for empty), or press Enter to use the provided default for that row.

---

## Example

```
 % python3 sudoku.py
Enter your Sudoku grid, one line at a time (9 digits per line, 0 = empty).
Press Enter to use the default row shown in brackets [].

Row 1 [306508400]:
Row 2 [520000000]:
Row 3 [087000031]:
Row 4 [003010080]:
Row 5 [900863005]:
Row 6 [050090600]:
Row 7 [130000250]:
Row 8 [000000074]:
Row 9 [005206300]:

Original Sudoku grid:
====================
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0

Sudoku solution:
====================
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9

Attempts to solve: 6732
```

The program will print the original and solved grids, and the number of attempts it took.

---

## Sample Puzzle

Paste this puzzle when prompted for rows:

- **Hard:**  
  ```
  000260701
  680070090
  190004500
  820100040
  004602900
  050003028
  009300074
  040050036
  703018000
  ```

---

## How It Works

- The script uses a recursive backtracking algorithm.
- It finds empty cells, tries valid numbers, and backtracks when stuck.
- The number of attempts is counted for visibility into the solving process.

---
