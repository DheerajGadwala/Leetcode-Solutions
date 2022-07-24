class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        for i in range(len(nums)):
            j, k = [i+1, len(nums)-1]
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ret.add((nums[i], nums[j], nums[k]))
                    k -= 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
        return ret