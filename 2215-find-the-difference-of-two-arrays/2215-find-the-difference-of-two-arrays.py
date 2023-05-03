class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ret1, ret2 = set(), set()
        for i in nums1:
            if i not in nums2:
                ret1.add(i)
        for i in nums2:
            if i not in nums1:
                ret2.add(i)
        return ret1, ret2