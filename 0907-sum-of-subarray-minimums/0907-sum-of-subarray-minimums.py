class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD=10**9+7
        n = len(arr)
        s = []
        l, r = [0] * n, [0] * n
        for i in range(n):
            j = i
            while len(s) > 0 and arr[i] <= s[-1][0]:
                j = s.pop()[1]
            s.append((arr[i], j))
            l[i] = i - j + 1
        s = []
        for i in range(n-1, -1, -1):
            j = i
            while len(s) > 0 and arr[i] < s[-1][0]:
                j = s.pop()[1]
            s.append((arr[i], j))
            r[i] = j - i + 1
        ans = 0
        for i in range(n):
            ans = (ans + l[i] * r[i] * arr[i]) % MOD
        return ans
        
        