class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        # BFS
        adj = {'a' : 'e', 'e' : 'ai', 'i' : 'aeou', 'o' : 'iu', 'u' : 'a'}
        q = [('a', 1), ('e', 1), ('i', 1), ('o', 1), ('u', 1)]
        count = {k:1 for k in q}
        cnt = 0
        MOD = 10**9 + 7
        
        while len(q) != 0:
            u = q.pop(0)
            curr, pos = u
            if pos == n:
                cnt += count[u]
                cnt %= MOD
                continue
            for c in adj[curr]:
                v = (c, pos + 1)
                if v not in count:
                    q.append((c, pos + 1))
                    count[v] = count[u]
                else:
                    count[v] += count[u]
                    count[v] %= MOD
        return cnt