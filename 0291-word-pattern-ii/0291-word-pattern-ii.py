class Solution:
    def wordPatternMatch(self, p: str, s: str) -> bool:
        pattern = dict()
        rev = dict()
        def res(i = 0, s = s):
            if i == len(p):
                return s == ''
            elif s == '':
                return False
            elif p[i] in pattern:
                pat = pattern[p[i]]
                ret = False
                for j in range(len(s)):
                    if s[:j+1] == pat:
                        ret |= res(i+1, s[j+1:])
                return ret
            else:
                ret = False
                for j in range(len(s)):
                    pat = s[:j+1]
                    if pat not in rev:
                        pattern[p[i]] = pat
                        rev[pat] = p[i]
                        ret |= res(i+1, s[j+1:])
                        del pattern[p[i]]
                        del rev[pat]
                return ret
        return res()