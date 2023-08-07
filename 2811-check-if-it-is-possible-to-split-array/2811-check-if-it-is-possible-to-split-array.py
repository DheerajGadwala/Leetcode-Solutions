class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) < 3:
            return True
        max_sum = 0        
        for i in range(1, len(nums)):                        
            max_sum = max(max_sum, sum(nums[i-1:i+1]))                   
        return max_sum >= m     