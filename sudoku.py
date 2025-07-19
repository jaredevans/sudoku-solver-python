from __future__ import annotations
import copy

# Type alias for a 9x9 Sudoku grid
Matrix = list[list[int]]

# Default Sudoku puzzle as strings (0 = empty cell)
DEFAULT_GRID_STRINGS = [
    "306508400",
    "520000000",
    "087000031",
    "003010080",
    "900863005",
    "050090600",
    "130000250",
    "000000074",
    "005206300",
]

def get_grid_from_input() -> Matrix:
    """
    Prompt the user to input a Sudoku puzzle row by row.
    Uses default rows if the user presses Enter.
    Returns the completed grid as a list of lists of integers.
    """
    grid = []
    print("Enter your Sudoku grid, one line at a time (9 digits per line, 0 = empty).")
    print("Press Enter to use the default row shown in brackets [].\n")
    for i in range(9):
        default = DEFAULT_GRID_STRINGS[i]
        while True:
            line = input(f"Row {i+1} [{default}]: ").strip()
            if line == "":
                line = default
            # Ensure input is 9 digits long and only contains digits
            if len(line) == 9 and all(c.isdigit() for c in line):
                grid.append([int(c) for c in line])
                break
            else:
                print("Invalid line. Please enter exactly 9 digits (0-9) or press Enter for default.")
    return grid

def is_safe(grid: Matrix, row: int, column: int, n: int) -> bool:
    """
    Check if it's safe to put digit n at grid[row][column].
    Ensures n is not already in the same row, column, or 3x3 box.
    """
    # Check row and column for n
    for i in range(9):
        if n in {grid[row][i], grid[i][column]}:
            return False
    # Check the 3x3 subgrid for n
    for i in range(3):
        for j in range(3):
            if grid[(row - row % 3) + i][(column - column % 3) + j] == n:
                return False                                                               return True

def find_empty_location(grid: Matrix) -> tuple[int, int] | None:
    """
    Find the next empty cell in the grid (cell with value 0).
    Returns a tuple (row, column) or None if there are no empty cells.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def sudoku(grid: Matrix, attempts: list[int]) -> Matrix | None:
    """
    Recursive backtracking solver for Sudoku.
    Tries to fill empty positions with digits 1-9 and backtracks on dead ends.
    Modifies the grid in place. Returns the solved grid, or None if no solution.
    Also counts the number of attempts via the 'attempts' list.
    """
    found = find_empty_location(grid)
    if not found:
        # Puzzle solved!
        return grid
    row, column = found
    for digit in range(1, 10):
        attempts[0] += 1  # Count each attempted placement
        if is_safe(grid, row, column, digit):
            grid[row][column] = digit
            if sudoku(grid, attempts) is not None:                                                     return grid  # Found a solution, return it up the recursion stack
            grid[row][column] = 0  # Backtrack
    return None  # Trigger backtracking if no valid digit found

def print_grid(grid: Matrix) -> None:
    """
    Print the Sudoku grid in a human-readable format.
    """
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()

if __name__ == "__main__":
    # Get the initial grid from the user (or use default)
    initial_grid = get_grid_from_input()
    print("\nOriginal Sudoku grid:\n" + "=" * 20)
    print_grid(initial_grid)
    print("Sudoku solution:\n" + "=" * 20)
    attempts = [0]  # Mutable list so attempt count can be updated in recursion
    # Deep copy so original grid isn't modified
    solution = sudoku(copy.deepcopy(initial_grid), attempts)
    if solution is not None:
        print_grid(solution)
        print(f"Attempts to solve: {attempts[0]}")
    else:
        print("Cannot find a solution.")

"""
Can copy and paste. Another one to solve:
000260701
680070090
190004500
820100040
004602900
050003028
009300074
040050036
703018000

Can copy and paste. This is a tough one:
020000000
000600003
074080000
000003002
080040010
600500000
000010780
500009000
000000040
"""
