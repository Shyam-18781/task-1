def print_grid(grid):
    """Helper function to print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    """Check if it's valid to place num at grid[row][col]."""

    if num in grid[row]:
        return False

    for r in range(9):
        if grid[r][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True

def find_empty_location(grid):
    """Find an empty location in the grid."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return None

def solve_sudoku(grid):
    """Solve the Sudoku grid using backtracking."""
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0

    return False

sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_grid):
    print("Sudoku solved successfully!")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")