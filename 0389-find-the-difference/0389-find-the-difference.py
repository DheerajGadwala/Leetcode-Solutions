class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        k = dict()
        for i in s:
            if i in k:
                k[i] += 1
            else:
                k[i] = 1
        for i in t:
            if i in k and k[i] != 0:
                k[i] -= 1
            else:
                return i