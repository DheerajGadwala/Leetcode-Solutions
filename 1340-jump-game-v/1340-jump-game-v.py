class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        s = []
        lb = [None]*n
        rb = [None]*n
        for i in range(n):
            while len(s) != 0 and arr[s[-1]] < arr[i]:
                s.pop()
            lb[i] = 0 if len(s) == 0 else s[-1]+1
            lb[i] = max(0, max(lb[i], i - d))
            s.append(i)
        s = []
        for i in range(n-1, -1, -1):
            while len(s) != 0 and arr[s[-1]] < arr[i]:
                s.pop()
            rb[i] = n if len(s) == 0 else s[-1]
            rb[i] = min(n, min(rb[i], i + d + 1))
            s.append(i)
        
        mem = dict()
        def dfs(u):
            if u in mem:
                return mem[u]
            else:
                ret = 0
                for i in range(lb[u], rb[u]):
                    if i != u:
                        ret = max(ret, dfs(i))
                mem[u] = 1 + ret
                return 1 + ret
        
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans