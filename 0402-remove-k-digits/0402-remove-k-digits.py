class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        nums = list(nums)
        i = 0
        while k > 0:
            if i+1 == len(nums):
                nums.pop()
                i -= 1
                k -= 1
            elif nums[i+1] >= nums[i]:
                i += 1
            else:
                nums.pop(i)
                i -= 1
                k -= 1
                i = max(0, i)
        while len(nums) != 0 and nums[0] == '0':
            nums.pop(0)
        return ''.join(nums) if len(nums) > 0 else '0'
        