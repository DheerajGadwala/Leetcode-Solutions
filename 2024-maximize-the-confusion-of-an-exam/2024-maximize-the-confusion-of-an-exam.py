class Solution:
    def maxConsecutiveAnswers(self, ak: str, k: int) -> int:
        i, j = 0, 0
        n = len(ak)
        ans, cnt = 0, 0
        while j < n:
            if ak[j] == 'T':
                j += 1
            elif cnt < k:
                j += 1
                cnt += 1
            elif ak[i] == 'F':
                i += 1
                cnt -= 1
            else:
                i += 1
            ans = max(ans, j - i)
        i, j, cnt = 0, 0, 0
        while j < n:
            if ak[j] == 'F':
                j += 1
            elif cnt < k:
                j += 1
                cnt += 1
            elif ak[i] == 'T':
                i += 1
                cnt -= 1
            else:
                i += 1
            ans = max(ans, j - i)
        return ans
                