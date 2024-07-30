class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        n = len(nums)
        pro = 1
        cnt = 0
        while j < n or i < n:
            if pro < k and j < n:
                cnt += j - i
                pro *= nums[j]
                j += 1
            elif i == j:
                i += 1
                j += 1
            elif pro >= k:
                pro /= nums[i]
                i += 1
            else:
                break
            
        return cnt + j - i