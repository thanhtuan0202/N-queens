import random
import numpy as np

class AStarAlgorithm:
    def __init__(self, n):
        self.n = n
        self.board = [random.randint(0, n - 1) for _ in range(n)]



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
        print("Step {} is: {}".format(0, self.board))
        count = 1
        while True:
            move = self.get_best_move()
            if move is None:
                if self.heuristic == 0:
                    break
                else:
                    new_board = [random.randint(0, self.n - 1) for _ in range(self.n)]
                    while np.array_equal(np.array(new_board), np.array(self.board)):
                        new_board = [random.randint(0, self.n - 1) for _ in range(self.n)]
                    self.board = new_board
            else:
                col, row = move
                self.move_queen(col, row)
                self.heuristic = self.calculate_heuristic()
                print("Step {} is: {}".format(count, self.board))
                count+=1
        return self.board

    def print_solution(self):

        for row in range(self.n):
            line = ['.'] * self.n
            line[self.board[row]] = 'Q'
            print(''.join(line))
        print('\n')


if __name__ == '__main__':
    n_queens = HillClimbingAlgorithm(8)
    res = n_queens.solve_n_queens()
    print(res)
    # n_queens.print_solution()
