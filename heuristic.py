import random


class AStarAlgorithm:
    pass


class HillClimbingAlgorithm:
    def __init__(self, n):
        self.n = n
        self.board = [random.randint(0, n - 1) for _ in range(n)]
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        heuristic = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == j - i:
                    heuristic += 1
        return heuristic

    def move_queen(self, col, row):
        self.board[col] = row

    def get_best_move(self):
        best_move = None
        min_heuristic = self.heuristic

        for col in range(self.n):
            for row in range(self.n):
                if self.board[col] != row:
                    prev_row = self.board[col]
                    self.move_queen(col, row)
                    new_heuristic = self.calculate_heuristic()
                    if new_heuristic < min_heuristic:
                        min_heuristic = new_heuristic
                        best_move = (col, row)
                    self.move_queen(col, prev_row)

        return best_move

    def solve_n_queens(self):
        while True:
            move = self.get_best_move()
            if move is None:
                break
            col, row = move
            self.move_queen(col, row)
            self.heuristic = self.calculate_heuristic()

    def print_solution(self):
        for row in range(self.n):
            line = ['.'] * self.n
            line[self.board[row]] = 'Q'
            print(''.join(line))
        print('\n')


if __name__ == '__main__':
    n_queens = HillClimbingAlgorithm(8)
    n_queens.solve_n_queens()
    n_queens.print_solution()
