class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l, h = 0, len(nums) - 1
        
        while l < h:
            
            m = (l + h) // 2
            
            a, b, c, d = [None] * 4
            
            if nums[m+1] == nums[m]:
                a, b, c, d = l, m-1, m+2, h
            
            elif nums[m-1] == nums[m]:
                a, b, c, d = l, m-2, m+1, h
            
            else:
                return nums[m]
            
            if (b - a) % 2 == 0:
                l, h = a, b
            else:
                l, h = c, d
        
        return nums[l]