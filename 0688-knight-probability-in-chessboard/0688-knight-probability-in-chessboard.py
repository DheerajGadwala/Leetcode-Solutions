class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        @cache
        def res(r = row, c = column, t = k):
            if r<0 or c<0 or r>=n or c>=n:
                return 0
            elif t == 0:
                return 1
            else:
                ret = 0
                x = [-1, 1]
                y = [-2, 2]
                for i in x:
                    for j in y:
                        ret += res(r+i, c+j, t-1)
                        ret += res(r+j, c+i, t-1)
                return ret
        
        return res()/8**k