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
        
        t = [[getChanges(j, i) for i in range(n)] for j in range(n)]

        @cache
        def res(st = 0, f = 0, k = k):
            if st == len(s) and f == len(s) and k == 0:
                return 0
            elif f == len(s) or k <= 0:
                return math.inf
            else:
                return min(t[st][f] + res(f+1, f+1, k-1), res(st, f+1, k))
        
        return res()