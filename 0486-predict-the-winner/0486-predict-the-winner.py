class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def res(i = 0, j = len(nums)-1):
            if i == j:
                return nums[i]
            else:
                return max(nums[i] - res(i+1, j), nums[j] - res(i, j-1))
        
        return res() >= 0