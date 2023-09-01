class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n, p = len(target), len(words[0]), len(words)
        
        mp = {i:{j:0 for j in 'qwertyuiopasdfghjklzxcvbnm'} for i in range(n)}
        for i in range(n):
            for j in range(p):
                mp[i][words[j][i]] += 1
                
        mod = 10**9+7
        @cache
        def res(pos = 0, k = 0):
            if pos == m:
                return 1
            elif k == n:
                return 0
            else:
                ret = res(pos, k+1) + mp[k][target[pos]] * res(pos+1, k+1)
                return ret % mod
            
        return res()