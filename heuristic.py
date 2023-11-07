import random
import numpy as np


class HillClimbingAlgorithm:
    def __init__(self, n):
        self.n = n
        self.board = [random.randint(0, n - 1) for _ in range(n)]
        self.heuristic = self.calculate_heuristic()

    def calculate_heuristic(self):
        attacking = 0
        # lưu current state của cột, đường chéo trái, phải
        dict1 = {}
        dict2 = {}
        dict3 = {}
        for i in range(self.n):
            # quân hậu đang xét có vị trí cột đã tồn tại trong dict
            if self.board[i] in dict1:
                attacking += 1
            else:
                dict1.update({self.board[i]: True})
            # quân hậu đang xét có vị trí đường chéo trái đã tồn tại trong dict
            if self.board[i] - i in dict2:
                attacking += 1
            else:
                dict2.update({self.board[i] - i: True})
            # quân hậu đang xét có vị trí đường chéo phải đã tồn tại trong dict
            if self.board[i] + i in dict3:
                attacking += 1
            else:
                dict3.update({self.board[i] + i: True})

        return attacking

    def move_queen(self, row, col):
        self.board[row] = col

    def get_best_move(self):
        best_move = None
        min_heuristic = self.heuristic

        for row in range(self.n):
            for col in range(self.n):
                if self.board[row] != col:
                    prev_col = self.board[row]
                    self.move_queen(row, col)
                    new_heuristic = self.calculate_heuristic()
                    if new_heuristic < min_heuristic:
                        min_heuristic = new_heuristic
                        best_move = (row, col)
                    self.move_queen(row, prev_col)

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
                    # flat problem
                    new_board = [random.randint(0, self.n - 1) for _ in range(self.n)]
                    while np.array_equal(np.array(new_board), np.array(self.board)):
                        new_board = [random.randint(0, self.n - 1) for _ in range(self.n)]
                    self.board = new_board
                    self.heuristic = self.calculate_heuristic()
                    print("Restart board: ", self.board)
            else:
                col, row = move
                self.move_queen(col, row)
                self.heuristic = self.calculate_heuristic()
                print("Step {} is: {}".format(count, self.board))
                count += 1
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
    n_queens.print_solution()
