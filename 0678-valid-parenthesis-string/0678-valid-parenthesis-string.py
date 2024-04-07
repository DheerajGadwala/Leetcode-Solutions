class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        @cache
        def res(i = 0, j = 0):
            if i == n:
                return j == 0
            elif s[i] == '(':
                return res(i+1, j+1)
            elif s[i] == ')':
                return j > 0 and res(i+1, j-1)
            else:
                return res(i+1, j) or res(i+1, j+1) or (j > 0 and res(i+1, j-1))
        return res()