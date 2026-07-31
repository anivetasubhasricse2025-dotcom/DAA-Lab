def is_safe(board, row, col):

    for prev_row in range(row):

        placed = board[prev_row]

        # Check same column
        if placed == col:
            return False

        # Check diagonal
        if abs(prev_row - row) == abs(placed - col):
            return False

    return True


def solve_n_queens(n):

    board = [-1] * n

    solutions = []

    backtrack_count = [0]

    def backtrack(row):

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):

            if is_safe(board, row, col):

                board[row] = col

                backtrack(row + 1)

                board[row] = -1

                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


def display_board(solution, n):

    print(" +" + "---+" * n)

    for row in range(n):

        print(" |", end="")

        for col in range(n):

            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()

        print(" +" + "---+" * n)
# ---------- Main Program ----------

for n in [4, 6, 8]:

    solutions, backtracks = solve_n_queens(n)

    print(f"\n========== {n}-Queens Problem ==========")

    print(f"Number of Solutions : {len(solutions)}")
    print(f"Backtracks          : {backtracks}")

    # ---------- Additional Analysis ----------

    if len(solutions) > 0:
        print("Solution Exists     : Yes")
    else:
        print("Solution Exists     : No")

    print(f"Queens Placed       : {n}")

    # Display all solutions only for N = 4
    if n == 4:

        print(f"\nAll Solutions for {n}-Queens:\n")

        for i, sol in enumerate(solutions, start=1):

            print(f"Solution {i}")

            print(f"Queen Positions : {sol}")

            display_board(sol, n)

    # ---------- Summary ----------

    print("Analysis:")
    print("- Backtracking places queens one row at a time.")
    print("- Unsafe positions are skipped immediately.")
    print("- The algorithm explores only valid possibilities.")
    print("- Program executed successfully.\n")