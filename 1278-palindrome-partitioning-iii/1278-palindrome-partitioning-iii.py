class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        n = len(s)
        
        def getChanges(i, j):
            ret = 0
            while i < j:
                if s[i] != s[j]:
                    ret += 1
                i += 1
                j -= 1
            return ret
        
        cost = [[getChanges(i, j) for j in range(n)] for i in range(n)]

        @cache
        def res(l = 0, r = 0, k = k):
            if l == len(s) and r == len(s) and k == 0:
                return 0
            elif r == len(s) or k <= 0:
                return math.inf
            else:
                return min(cost[l][r] + res(r + 1, r + 1, k - 1), res(l, r +1, k))
        
        return res()