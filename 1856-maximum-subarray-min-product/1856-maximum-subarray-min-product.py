class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        s = []
        n = len(nums)
        r, l = [None] * n, [None] * n
        for i in range(n):
            while len(s) > 0 and nums[s[-1]] > nums[i]:
                r[s.pop()] = i
            s.append(i)
        while len(s) != 0:
            r[s.pop()] = n
        s = []
        for i in range(n-1, -1, -1):
            while len(s) > 0 and nums[s[-1]] > nums[i]:
                l[s.pop()] = i + 1
            s.append(i)
        while len(s) != 0:
            l[s.pop()] = 0
        rs = [0]
        for i in nums:
            rs.append(rs[-1] + i)
        ans = 0
        for i in range(n):
            ans = max(ans, nums[i] * (rs[r[i]] - rs[l[i]]))
        return ans % (10**9+7)
            
            