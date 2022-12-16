class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        n = len(nums)
        found = False
        
        for i in range(1, n):
            a = nums[i-1]
            b = nums[i]
            
            if a > b:
                
                if found:
                    return False
                
                found = True
                
                if i == 1:
                    nums[0] = nums[1]
                else:
                    c = nums[i-2]
                    if c <= b:
                        nums[i-1] = c
                    else:
                        nums[i] = a
        return True