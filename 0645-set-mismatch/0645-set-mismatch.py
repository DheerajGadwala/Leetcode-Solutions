class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        dup = None
        n = len(nums)
        
        for i in nums:
            if nums[abs(i) - 1] < 0:
                dup = abs(i)
                break
            else:
                nums[abs(i) - 1] *= -1
        
        return [dup, n * (n + 1) // 2 - sum([-i if i < 0 else i for i in nums]) + dup]