class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [0]*n
        count = [1]*n
        max_length = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j] + 1:
                        count[i] += count[j]
                    elif length[i] < length[j] + 1:
                        count[i] = count[j]
                        length[i] = length[j] + 1
            max_length = max(max_length, length[i])
        ans = 0
        for i in range(n):
            if length[i] == max_length:
                ans += count[i]
        return ans
                    
