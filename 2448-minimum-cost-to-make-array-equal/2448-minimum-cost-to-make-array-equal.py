class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        nc = [[nums[i], cost[i]] for i in range(n)]
        nc.sort(key = lambda x: x[0])
        curr = 0
        for i in range(n):
            curr += abs(nc[0][0] - nc[i][0]) * nc[i][1]
        for i in range(1, n):
            nc[i][1] += nc[i-1][1]
        ans = curr
        for i in range(1, n):
            diff = nc[i][0] - nc[i-1][0]
            curr += nc[i-1][1] * diff
            curr -= (nc[-1][1] - nc[i-1][1]) * diff
            ans = min(ans, curr)
        return ans