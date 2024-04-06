class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stk = []
        for i in range(len(s)):
            if s[i] not in '()':
                continue
            elif s[i] == '(':
                stk.append(i)
            elif len(stk) > 0:
                stk.pop()
            else:
                s[i] = '*'
        for i in stk:
            s[i] = '*'
        ret = []
        for i in s:
            if i != '*':
                ret.append(i)
        return ''.join(ret)
            