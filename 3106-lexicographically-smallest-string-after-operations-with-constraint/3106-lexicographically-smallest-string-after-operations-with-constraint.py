class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        
        s = list(s)
        n = len(s)
        alph = 'abcdefghijklmnopqrstuvwxyz'
        i = 0
        
        @cache
        def minDist(a, b):
            a = ord(a) - ord('a')
            b = ord(b) - ord('a')
            a, b = min(a, b), max(a, b)
            ret = b - a
            i = 0
            while b != a:
                i += 1
                b += 1
                b %= 26
            return min(ret, i)
        
        while i < n:
            for j in alph:
                if minDist(s[i], j) <= k:
                    k -= minDist(s[i], j)
                    s[i] = j
                    break
            i += 1
        
        return ''.join(s)
            