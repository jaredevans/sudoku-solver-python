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
    git clone https://github.com/YOUR-USERNAME/sudoku-solver-python.git
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
Enter your Sudoku grid, one line at a time (9 digits per line, 0 = empty).
Press Enter to use the default row shown in brackets [].

Row 1 [306508400]: 000260701
Row 2 [520000000]: 
...
```

The program will print the original and solved grids, and the number of attempts it took.

---

## Sample Puzzles

Paste one of these when prompted for rows:

- **Normal:**  
  ```
  306508400
  520000000
  087000031
  003010080
  900863005
  050090600
  130000250
  000000074
  005206300
  ```

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
