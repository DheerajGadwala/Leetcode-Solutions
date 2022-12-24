class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        m = len(rides)
        
        rides.sort(key = lambda x: x[1])
        
        cache = [0] * (n + 1)
        
        j = 0
        
        for i in range(1, n + 1):
            
            cache[i] = cache[i - 1]
            
            while j < m and rides[j][1] == i:
                
                s, e, t = rides[j]
                
                cache[i] = max(cache[i], cache[s] + e - s + t)
                
                j += 1
        
        return cache[-1]