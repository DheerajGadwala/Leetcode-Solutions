class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def res(i = 0, j = 0, k = 0):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            ret = False
            if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
                ret |= res(i+1, j, k+1)
            if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
                ret |= res(i, j+1, k+1)
            return ret
        return res()