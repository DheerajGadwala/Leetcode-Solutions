class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        splitPoint = 0
        
        def binSplit(l, h):
            nonlocal splitPoint
            if l <= h:
                m = (l + h) // 2
                if nums[m] < nums[m-1]:
                    splitPoint = m
                else:
                    binSplit(m+1, h)
                    binSplit(l, m - 1)
        
        def binSearch(l, h):
            if l <= h:
                m = (l + h) // 2
                if nums[m] == target:
                    return True
                elif nums[m] > target:
                    return binSearch(l, m - 1)
                else:
                    return binSearch(m + 1, h)
            return False
        
        binSplit(0, len(nums) - 1)
        
        return binSearch(0, splitPoint - 1) or binSearch(splitPoint, len(nums) - 1)
        
                    
            