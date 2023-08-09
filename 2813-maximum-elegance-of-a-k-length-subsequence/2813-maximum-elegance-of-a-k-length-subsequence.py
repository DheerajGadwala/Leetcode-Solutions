class Solution:
    
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        
        items.sort(key = lambda x: -x[0])
        pro, cats = 0, set()
        removable = []
        n = len(items)
        for i in range(k):
            pro+=items[i][0]
            if items[i][1] in cats:
                heappush(removable, items[i][0])
            cats.add(items[i][1])
        score = pro + len(cats)**2
        mx = score
        for i in range(k, n):
            if len(cats) == k:
                break
            if items[i][1] not in cats:
                score -= heappop(removable)
                score -= len(cats)**2
                cats.add(items[i][1])
                score += items[i][0]
                score += len(cats)**2
                mx = max(mx, score)
        return mx
        
        
        
        
        
        """
        DP TLE
        n = len(items)
        items.sort(key = lambda x: x[1])
        
        @cache
        def res(i = 0, q = 0, prev = 0, cnt = 0):
            if q == k:
                return 0
            elif i == n:
                return -math.inf
            elif prev == items[i][1]:
                return max(items[i][0] + res(i+1, q+1, prev, cnt), res(i+1, q, prev, cnt))
            else:
                return max(-cnt**2+(cnt+1)**2+items[i][0]+res(i+1, q+1, items[i][1], cnt+1), res(i+1, q, prev, cnt))
        
        return res()
        """