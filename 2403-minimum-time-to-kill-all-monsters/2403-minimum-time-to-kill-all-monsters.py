class Solution:
    def minimumTime(self, power: List[int]) -> int:
        
        @cache
        def res(gain = 1, mask = 0):
            if gain > len(power):
                return 0
            else:
                ans = math.inf
                j = 1
                for i in range(len(power)):
                    if j & mask == 0:
                        days = math.ceil(power[i] / gain)
                        ans = min(ans, days + res(gain + 1, mask | j))
                    j <<= 1
                return ans
        
        return res()