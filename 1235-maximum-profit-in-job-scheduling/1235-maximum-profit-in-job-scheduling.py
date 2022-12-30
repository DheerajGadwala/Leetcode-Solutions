class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n = len(startTime)
        
        events = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        
        days = [0]
        scores = {0:0}
        
        events.sort(key = lambda x: x[1])
        
        for s, e, v in events:
            
            l, h = 0, len(days) - 1
            floor = None
            
            while l <= h:
                
                m = (l + h) // 2
                
                if days[m] <= s:
                    floor = days[m]
                    l = m + 1
                
                else:
                    h = m - 1
            
            scores[e] = max(scores.get(e, 0), scores.get(floor) + v, scores[days[-1]])
            
            if days[-1] != e:
                days.append(e)
        
        # print(scores)
        
        return scores[days[-1]]
        
            