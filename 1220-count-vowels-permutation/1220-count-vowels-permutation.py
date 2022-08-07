class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        adj = {'a' : 'e', 'e' : 'ai', 'i' : 'aeou', 'o' : 'iu', 'u' : 'a'}
        MOD = 10**9 + 7
        
        @cache
        def res(pos, curr):
            if pos == n:
                return 1
            ret = 0
            for c in adj[curr]:
                ret = (ret + res(pos + 1, c)) % MOD
            return ret
        
        return (sum([res(1, c) for c in adj])) % MOD