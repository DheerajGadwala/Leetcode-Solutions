class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ret = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                k, l = j + 1, n - 1
                s_par = nums[i] + nums[j]
                while k < l:
                    s = nums[k] + nums[l] + s_par
                    if s > target:
                        l -= 1
                    elif s < target:
                        k += 1
                    else:
                        ret.add((nums[i], nums[j], nums[k], nums[l]))
                        l -= 1
        return ret
                    