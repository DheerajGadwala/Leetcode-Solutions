class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        d = dict()
        rd = dict()
        n = len(s)
        
        if len(pattern) != len(s):
            return False
        
        for i in range(n):
            if pattern[i] not in d and s[i] not in rd:
                d[pattern[i]] = s[i]
                rd[s[i]] = pattern[i]
            elif pattern[i] not in d or s[i] not in rd or d[pattern[i]] != s[i]:
                return False
        
        return True
            