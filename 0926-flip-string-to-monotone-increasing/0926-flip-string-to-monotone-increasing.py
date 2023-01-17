class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        @cache
        def res(pos = 0, curr = '0'):
            if pos == len(s):
                return 0
            elif s[pos] == curr:
                return res(pos + 1, curr)
            elif s[pos] == '0' and curr == '1':
                return 1 + res(pos + 1, '1')
            elif s[pos] == '1' and curr == '0':
                return min(1 + res(pos + 1), res(pos + 1, '1'))
        
        return res()