class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        n = len(events)
        
        events.sort(key = lambda x: x[0])
        
        j = 0
        
        lastDay = max([e[1] for e in events])
        
        ans = 0
        
        q = []
        
        for i in range(1, lastDay+1):
            
            while j < n and events[j][0] == i:
                heappush(q, events[j][1])
                j += 1
            
            while len(q) > 0 and q[0] < i:
                heappop(q)
            
            if len(q) > 0:
                heappop(q)
                ans += 1
        
        return ans
            