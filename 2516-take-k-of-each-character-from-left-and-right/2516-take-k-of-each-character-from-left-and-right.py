class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        mp = {i:-k for i in 'abc'}
        for i in s:
            mp[i] += 1
        i, j = 0, 0
        curr = {i:0 for i in 'abc'}
        ans = -1
        while j < n and i < n:
            c = s[j]
            if curr[c] < mp[c]:
                curr[c] += 1
                j += 1
            else:
                curr[s[i]] -= 1
                i += 1
            flag = True
            for k in 'abc':
                flag &= curr[k] <= mp[k]
            if flag:        
                ans = max(ans, j - i)
        return -1 if ans < 0 else len(s) - ans
            