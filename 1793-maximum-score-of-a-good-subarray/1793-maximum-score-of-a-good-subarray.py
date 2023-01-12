class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        nums.append(-math.inf)
        n = len(nums)
        s = []
        ans = -math.inf
        
        for i in range(n):
            multiplier = i
            while len(s) > 0 and nums[s[-1][0]]  >= nums[i]:
                if s[-1][1] <= k and k < i:
                    ans = max(ans, nums[s[-1][0]] * (i - s[-1][1]))
                multiplier = s.pop()[1]
            s.append((i, multiplier))
        
        return ans