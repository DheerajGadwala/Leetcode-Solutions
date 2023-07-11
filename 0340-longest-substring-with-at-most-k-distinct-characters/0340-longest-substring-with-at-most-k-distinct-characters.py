class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        i, j = 0, 0
        win = dict()
        ans = 0
        while j < len(s):
            if len(win) < k or (len(win) == k and s[j] in win):
                win[s[j]] = win.get(s[j], 0) + 1
                j += 1
            else:
                win[s[i]] = win.get(s[i], 0) - 1
                if win[s[i]] == 0:
                    del win[s[i]]
                i += 1
            ans = max(ans, j - i)
        return ans
                