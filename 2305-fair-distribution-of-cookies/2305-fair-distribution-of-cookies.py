class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = sum(cookies)
        N = len(cookies)
        total = [0]*k
        
        def backtrack(i, total):
            nonlocal ans
            if i == N:
                ans = min(ans, max(total))
                return
            
            if max(total) >= ans:
                return
            
            for j in range(k):
                total[j] += cookies[i]
                backtrack(i+1, total)
                total[j] -= cookies[i]
        

        backtrack(0, total)
        return ans