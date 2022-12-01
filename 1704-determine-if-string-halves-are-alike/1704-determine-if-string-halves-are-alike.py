class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        l = [i.lower() if i in 'aeiouAEIOU' else "" for i in s[:n]]
        r = [i.lower() if i in 'aeiouAEIOU' else "" for i in s[n:]]
        l = ''.join(l)
        r = ''.join(r)
        return len(l) == len(r)