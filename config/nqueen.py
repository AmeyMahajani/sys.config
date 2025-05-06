def solve_n_queens(n):
    board = [-1] * n  # board[i] = column of queen in row i
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # row + col
    diag2 = [False] * (2 * n - 1)  # row - col + (n - 1)
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                board[row] = col
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                backtrack(row + 1)
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False
                board[row] = -1

    backtrack(0)

    for sol in solutions:
        for row in sol:
            print("".join("Q" if i == row else "|-|" for i in range(n)))
        print()

# Example: Solve for 4 queens
solve_n_queens(4)
