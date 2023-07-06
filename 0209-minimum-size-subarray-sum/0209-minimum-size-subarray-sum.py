class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        curr = 0
        ans = math.inf
        while j < n or i < n:
            if curr < target and j < n:
                curr += nums[j]
                j += 1
            elif curr >= target:
                curr -= nums[i]
                i += 1
            else:
                break
            if curr >= target:
                ans = min(ans, j - i)
        return 0 if ans == math.inf else ans
                