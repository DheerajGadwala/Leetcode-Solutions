class Solution:
    def maximumTastiness(self, prices: List[int], k: int) -> int:
        prices.sort()
        l, h = 1, 10**9
        ans = 0
        while l <= h:
            
            m = (l + h) // 2
            
            cnt = 1
            nxt = prices[0] + m
            for i in range(1, len(prices)):
                if prices[i] >= nxt:
                    nxt = prices[i] + m
                    cnt += 1
            
            if cnt < k:
                
                h = m - 1
            
            else:
                ans = m
                l = m + 1
        
        return ans