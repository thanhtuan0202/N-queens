import unittest
from heuristic import *
from dfs import *
from bfs import *


def is_valid(board):
    exist_col: [int] = []
    diag1: [int] = []
    diag2: [int] = []
    for i in range(len(board)):
        col = board[i]
        if (col in exist_col) or (col + i in diag1) or (col - i in diag2):
            return False
        exist_col.append(col)
        diag1.append(col + i)
        diag2.append(col - i)
    return True


class CheckSolution(unittest.TestCase):

    # def test_bfs_1(self):
    #     n = 4
    #     bfs = BFS()
    #     res = bfs.solution(n)
    #     self.assertTrue(is_valid(res))
    #
    # def test_bfs_2(self):
    #     n = 5
    #     bfs = BFS()
    #     res = bfs.solution(n)
    #     self.assertTrue(is_valid(res))
    #
    # def test_bfs_3(self):
    #     n = 6
    #     bfs = BFS()
    #     res = bfs.solution(n)
    #     self.assertTrue(is_valid(res))
    #
    # def test_dfs_1(self):
    #     n = 4
    #     dfs = DFS()
    #     res = dfs.solution(n)
    #     self.assertTrue(is_valid(res))
    #
    # def test_dfs_2(self):
    #     n = 5
    #     dfs = DFS()
    #     res = dfs.solution(n)
    #     self.assertTrue(is_valid(res))
    #
    # def test_dfs_3(self):
    #     n = 6
    #     dfs = DFS()
    #     res = dfs.solution(n)
    #     self.assertTrue(is_valid(res))

    def test_heuristic_1(self):
        n = 8
        sol = HillClimbingAlgorithm(n)
        res = sol.solve_n_queens()
        print(res)
        self.assertTrue(is_valid(res))

if __name__ == '__main__':
    unittest.main()
