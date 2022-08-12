class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        tar = abs(goal - s)
        return math.ceil(tar / limit) 
                
        