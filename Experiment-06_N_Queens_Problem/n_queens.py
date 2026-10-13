"""
EXPERIMENT 6: Implementation of N-Queens Problem (where 1 <= N <= 9)
Course: AI Lab Practical (CSE)
Description:
    Solves the classic N-Queens problem using Backtracking algorithm.
    Validates constraint 1 <= N <= 9, prints visual board representations,
    queen coordinates, and total count of distinct valid solutions.
"""

import sys


class NQueensSolver:
    def __init__(self, n):
        if not (1 <= n <= 9):
            raise ValueError(f"Constraint Violation: N must be between 1 and 9 (Received N = {n})")
        self.n = n
        self.solutions = []
        self.board = [["." for _ in range(n)] for _ in range(n)]

    def is_safe(self, row, col):
        """
        Check if placing a Queen at (row, col) is safe.
        Since queens are placed column by column from left to right,
        we only need to check the left side.
        """
        # 1. Check current row on left side
        for c in range(col):
            if self.board[row][c] == "Q":
                return False

        # 2. Check upper diagonal on left side
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if self.board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        # 3. Check lower diagonal on left side
        r, c = row + 1, col - 1
        while r < self.n and c >= 0:
            if self.board[r][c] == "Q":
                return False
            r += 1
            c -= 1

        return True

    def solve(self, col=0):
        """
        Backtracking recursive solver:
        Tries to place a queen in every row of the current column.
        """
        # Base case: If all queens are placed successfully
        if col == self.n:
            # Save a snapshot of the completed board
            solution_snapshot = [list(r) for r in self.board]
            self.solutions.append(solution_snapshot)
            return

        for row in range(self.n):
            if self.is_safe(row, col):
                # Place queen
                self.board[row][col] = "Q"

                # Recurse for next column
                self.solve(col + 1)

                # Backtrack: remove queen and try next row
                self.board[row][col] = "."

    def get_queen_positions(self, solution_board):
        """Returns list of (row, col) coordinates for all queens."""
        positions = []
        for r in range(self.n):
            for c in range(self.n):
                if solution_board[r][c] == "Q":
                    positions.append((r, c))
        return positions

    def print_board(self, solution_board, solution_num):
        """Prints formatted 2D chessboard layout."""
        print(f"\n--- Solution #{solution_num} ---")
        positions = self.get_queen_positions(solution_board)
        print(f"Queen Coordinates (Row, Col): {positions}")
        print("+" + "---+" * self.n)
        for r in range(self.n):
            row_str = "| " + " | ".join(solution_board[r]) + " |"
            print(row_str)
            print("+" + "---+" * self.n)


def display_n_queens(n):
    print("=" * 70)
    print(f"SOLVING {n}-QUEENS PROBLEM (N = {n}, Constraint: 1 <= N <= 9)")
    print("=" * 70)

    solver = NQueensSolver(n)
    solver.solve()

    total_solutions = len(solver.solutions)
    print(f"Total distinct valid solutions found for N = {n}: {total_solutions}")

    if total_solutions == 0:
        print(f"No solution exists for N = {n} on a {n}x{n} chessboard.")
    else:
        # Show first 2 solutions (or all if <= 2)
        show_limit = min(2, total_solutions)
        for i in range(show_limit):
            solver.print_board(solver.solutions[i], i + 1)

        if total_solutions > show_limit:
            print(f"\n... and {total_solutions - show_limit} other valid solutions.")


def print_theoretical_solutions_table():
    """Prints standard reference table of solutions for N = 1 to 9."""
    table = [
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 2),
        (5, 10),
        (6, 4),
        (7, 40),
        (8, 92),
        (9, 352),
    ]
    print("\n" + "=" * 70)
    print("N-QUEENS THEORETICAL SOLUTION COUNT REFERENCE TABLE (N = 1 to 9):")
    print("=" * 70)
    print(f"{'N (Board Size)':<18} | {'Total Solutions':<18} | {'Feasibility':<20}")
    print("-" * 70)
    for n_val, sol_count in table:
        feasibility = "No solution possible" if sol_count == 0 else f"{sol_count} solutions exist"
        print(f"{f'{n_val} x {n_val}':<18} | {sol_count:<18} | {feasibility:<20}")
    print("=" * 70)


def main():
    # If user provided N as command line argument
    if len(sys.argv) > 1:
        try:
            n_arg = int(sys.argv[1])
            display_n_queens(n_arg)
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
    else:
        # Default run demonstrates N=4 and N=8, followed by reference table
        print("Running demonstration for N = 4 (Classic exam problem):")
        display_n_queens(4)

        print("\n" + "=" * 70)
        print("Running demonstration for N = 8 (Standard 8-Queens):")
        display_n_queens(8)

        print_theoretical_solutions_table()


if __name__ == "__main__":
    main()
