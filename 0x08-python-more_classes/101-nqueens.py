#!/usr/bin/python3
import sys


def print_solutions(solutions):
    """Prints the solutions in the required format."""

    for solution in solutions:
        print(solution)


def is_not_under_attack(row, col, queens):
    """Checks if a queen can be placed at (row, col)."""
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_nqueens(n, row=0, queens=[]):
    """Uses backtracking to find all sos to the N Queens problem."""
    if row == n:
        solutions.append(queens[:])
        return

    for col in range(n):
        if is_not_under_attack(row, col, queens):
            queens.append([row, col])
            solve_nqueens(n, row + 1, queens)
            queens.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    global solutions
    solutions = []
    solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
