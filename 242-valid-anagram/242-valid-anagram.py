class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = dict(), dict()
        for i in s:
            a[i] = 1 if i not in a else a[i] + 1
        for i in t:
            b[i] = 1 if i not in b else b[i] + 1
        if len(a) != len(b):
            return False
        for i in a:
            if i not in b:
                return False
            elif a[i] != b[i]:
                return False
        return True