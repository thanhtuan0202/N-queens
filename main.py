from bfs import *
from dfs import *


def is_valid(board):
    exist_col: [int] = []
    diag1: [int] = []
    diag2: [int] = []
    for i in range(len(board)):
        row = board[i]
        if (i in exist_col) or (row + i in diag1) or (row - i in diag2):
            return False
        exist_col.append(i)
        diag1.append(row + i)
        diag2.append(row - i)
    return True

if __name__ == "__main__":
    # n = 4
    # dfs = DFS()
    # lst = dfs.solution(8)

    bfs = BFS()
    lst = bfs.solution(8)
    # for i in range(len(lst)):
    #     print(lst[i])
    print(lst)
    # print(is_valid(lst))
