import random


class DFS:
    def __init__(self):
        self.res = []
        self.exist_col: [int] = []
        self.diag1: [int] = []
        self.diag2: [int] = []

    def dfs(self, n, row, res, lst):
        if row == n:
            res.append(lst[:])
            return
        for i in range(n):
            if (i in self.exist_col) or (row + i in self.diag1) or (row - i in self.diag2):
                continue
            newlst = [0 for _ in range(n)]
            newlst[i] = 1
            lst.append(newlst[:])
            self.exist_col.append(i)
            self.diag1.append(row + i)
            self.diag2.append(row - i)

            self.dfs(n, row + 1, res, lst)

            lst.remove(newlst)
            self.exist_col.remove(i)
            self.diag1.remove(row + i)
            self.diag2.remove(row - i)

    def solution(self, n):
        lst = []
        self.dfs(n, 0, self.res, lst)
        return self.convert_solution(n)

    def convert_solution(self, n):
        lst = []
        ran = random.choice(self.res)
        for i in range(n):
            for j in range(n):
                if ran[i][j] == 1:
                    lst.append(j)
                    break
        return lst
