class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        l = [i-1 for i in range(n)]
        r = [i+1 for i in range(n)]
        q = []
        dist = dict()
        ans = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                q.append(i)
                dist[i] = 1
                ans = 1
        while len(q) != 0:
            u = q.pop(0)
            ans = max(ans, dist[u])
            if r[u] < n:
                l[r[u]] = l[u]
            if l[u] > -1:
                r[l[u]] = r[u]
            if r[u] not in dist and r[u] < n and nums[r[u]] < nums[l[u]]:
                dist[r[u]] = dist[u] + 1
                q.append(r[u])
        return ans
            
            