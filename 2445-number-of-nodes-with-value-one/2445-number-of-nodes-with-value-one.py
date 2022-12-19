class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        tree = [0] * (n + 1)
        for q in queries:
            tree[q] += 1
        
        def res(pos = 1, val = 0):
            if pos > n:
                return 0
            else:
                s = (tree[pos] + val) % 2
                return s + res(pos*2, s) + res(pos*2+1, s)
        
        return res()