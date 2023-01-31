class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        for i in range(n-1, k-1, -1):
            nums[i] -= nums[i-k]
        nums = nums[k-1:]
        
        n = len(nums)
        
        @cache
        def res(pos = 0, a = 3):
            nonlocal n, k
            if a == 0:
                return [[], 0]
            elif pos >= n:
                return [[], -math.inf]
            else:
                x = res(pos + 1, a)
                y = res(pos + k, a - 1)
                x = x[:]
                y = y[:]
                y[1] += nums[pos]
                y[0] = [pos] + y[0]
                if x[1] > y[1]:
                    return x
                elif y[1] > x[1]:
                    return y
                elif x[0] < y[0]:
                    return x
                else:
                    return y
                
        return res()[0]