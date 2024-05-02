class NQueensBacktracking:
    def __init__(self, n):
        self.n = n
        self.board = [['-' for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check column
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        
        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False
        
        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 'Q':
                return False
        
        return True

    def solve(self, row):
        if row == self.n:
            self.solutions.append([' '.join(row) for row in self.board])
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.solve(row + 1)
                self.board[row][col] = '-'

    def get_solutions(self):
        self.solve(0)
        return self.solutions

# Get user input for board size
n = int(input("Enter the size of the board (n x n): "))

solver = NQueensBacktracking(n)
solutions = solver.get_solutions()
print(f"Number of solutions for {n}-Queens problem: {len(solutions)}")
for solution in solutions:
    print("\n".join(solution))
    print()
