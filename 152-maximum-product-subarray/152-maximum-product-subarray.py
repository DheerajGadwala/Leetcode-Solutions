class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        mn = mx = ans = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] >= 0:
                mx, mn = max(mx * nums[i], nums[i]), min(mn * nums[i], nums[i])
            else:
                mx, mn = max(mn * nums[i], nums[i]), min(mx * nums[i], nums[i])
        
            ans = max(ans, mx)
        
        return ans
