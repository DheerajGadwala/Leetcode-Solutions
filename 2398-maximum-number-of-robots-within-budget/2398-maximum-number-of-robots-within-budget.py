class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        q = []
        f, l, currSum, ans, n = 0, 0, 0, 0, len(chargeTimes)
        
        while (f < n):
            while (len(q) != 0 and chargeTimes[q[-1]] < chargeTimes[f]): 
                q.pop()
            q.append(f)
            currSum += runningCosts[f]
            f += 1
            while (l != f and chargeTimes[q[0]] + (f-l) * currSum > budget):
                if q[0] == l:
                    q.pop(0)
                currSum -= runningCosts[l]
                l += 1
            ans = max(ans, f-l)
        
        return ans
            