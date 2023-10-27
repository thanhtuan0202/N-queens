class Nqueens:
    def __init__(self):
        self.exist_col: [int] = []
        self.diag1: [int] = []
        self.diag2: [int] = []

    # def is_safe(self, board, row, col):
    #     for i in range(row):
    #         if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
    #             return False
    #     return True

    def bfs(self, res, n):
        queue = [[]]
        lst = [[]]
        while queue:
            board = queue.pop(0)
            crlist = lst.pop(0)
            if len(board) == n:
                res.append(board)
            else:
                if len(crlist) == 3:
                    self.exist_col = crlist[0]
                    self.diag1 = crlist[1]
                    self.diag2 = crlist[2]
                row = len(board)
                for i in range(n):
                    if (i in self.exist_col) or (row + i in self.diag1) or (row - i in self.diag2):
                        continue
                    queue.append(board + [i])
                    newlist = [self.exist_col + [i], self.diag1 + [row + i], self.diag2 + [row - i]]
                    lst.append(newlist)
        return res

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
        res = []
        lst = []
        # self.dfs(n, 0, res, lst)
        self.bfs(res, n)
        return res



if __name__ == "__main__":
    n = 4
    nqueen = Nqueens()
    lst = nqueen.solution(4)
    for i in range(len(lst)):
        print(lst[i])
