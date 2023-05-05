class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        vc = 0
        i = 0
        while i < k:
            if s[i] in vowels:
                vc += 1
            i += 1
        ans = vc
        while i < len(s):
            if s[i-k] in vowels:
                vc -= 1
            if s[i] in vowels:
                vc += 1
            ans = max(ans, vc)
            i += 1
        return ans