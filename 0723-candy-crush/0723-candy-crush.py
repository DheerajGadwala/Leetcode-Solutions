class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        
        def markForCrush(board):
            cont = False
            marked = [[False] * n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0:
                        continue
                    k = 0
                    while i + k < m and board[i][j] == board[i+k][j]:
                        k+=1
                    if k > 2:
                        k = 0
                        while i + k < m and board[i][j] == board[i+k][j]:
                            marked[i+k][j] = True
                            k += 1
                    k = 0
                    while j + k < n and board[i][j] == board[i][j+k]:
                        k += 1
                    if k > 2:
                        k = 0
                        while j + k < n and board[i][j] == board[i][j+k]:
                            marked[i][j+k] = True
                            k += 1
            cont = False
            for i in range(m):
                for j in range(n):
                    if marked[i][j]:
                        board[i][j] = 0
                    cont |= marked[i][j]
            return cont
        
        def crush(board):
            for i in range(n):
                j, k = m-1, m-1
                while j > -1:
                    if board[j][i] != 0:
                        board[k][i] = board[j][i]
                        j -= 1
                        k -= 1
                    else:
                        j -= 1
                while k > -1:
                    board[k][i] = 0
                    k -= 1
        i = 0
        while markForCrush(board):
            crush(board)
            i+=1
        
        return board