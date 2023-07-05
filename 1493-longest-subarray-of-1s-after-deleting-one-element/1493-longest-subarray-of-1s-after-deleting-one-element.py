class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        zeroPosition = None
        ans = 0
        while j < n:
            if nums[j] != 0:
                j += 1
            elif zeroPosition is None:
                zeroPosition = j
                j += 1
            else:
                i = zeroPosition + 1
                zeroPosition = j
                j += 1
            ans = max(ans, j - i - 1)
        
        return ans
                
                