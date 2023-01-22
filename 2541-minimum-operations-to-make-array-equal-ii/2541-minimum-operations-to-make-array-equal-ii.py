class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2:
                return 0
            else:
                return -1
        n = len(nums1)
        chg = 0
        ans = 0
        for i in range(n):
            diff = nums1[i] - nums2[i]
            print(i, diff, diff // k)
            if diff % k != 0:
                return -1
            chg += diff // k
            ans += abs(diff // k)
        
        return ans // 2 if chg == 0 else -1