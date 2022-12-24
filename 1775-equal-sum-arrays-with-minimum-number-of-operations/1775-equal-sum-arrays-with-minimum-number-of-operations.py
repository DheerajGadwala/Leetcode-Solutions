class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        x, y = sum(nums1), sum(nums2)
        
        if x < y:
            nums1, nums2 = nums2, nums1
            x, y = y, x
        
        nums1.sort()
        nums2.sort()
        nums1.insert(0, -1)
        nums2.append(7)
        
        m, n = len(nums1), len(nums2)
        
        i, j = m - 1, 0
        cnt = 0
        
        while x > y:
            
            if i == 0 and j == n - 1:
                return -1
            
            a, b = nums1[i] - 1, 6 - nums2[j]
            if a >= b:
                i -= 1
                x -= a
            else:
                j += 1
                y += b
            
            cnt += 1
        
        return cnt