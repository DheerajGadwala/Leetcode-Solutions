class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        m = None
        while l <= h:
            # print(l, h)
            # print(nums[l:h+1])
            m = (l + h) // 2
            if nums[m-1] > nums[m]:
                break
            elif nums[m] < nums[l]:
                h = m - 1
            elif nums[m] > nums[h]:
                l = m + 1
            else:
                m = l
                break
        
        l = 0
        h = m - 1
        
        # print(m)
        # print(nums[:m], nums[m+1:])
        
        def binSearch(l, h):
            while l < h:
                m = (l + h) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    h = m - 1
                else:
                    l = m + 1
            return l
        
        x = binSearch(0, m - 1)
        y = binSearch(m, len(nums) - 1)
        
        return x if nums[x] == target else y if nums[y] == target else -1 
            