class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        e = dict()
        for i in range(n):
            e[i] = set()
        for i in roads:
            e[i[0]].add(i[1])
            e[i[1]].add(i[0])
        m1 = -math.inf
        m1n = None
        m2 = -math.inf
        m2n = None
        for i in e:
            if len(e[i]) > m1:
                m2 = m1
                m2n = m1n
                m1 = len(e[i])
                m1n = i
            elif len(e[i]) > m2:
                m2 = len(e[i])
                m2n = i
            elif len(e[i]) == m1 and i not in e[m2n]:
                m1n = i
            elif len(e[i]) == m2 and i not in e[m1n]:
                m2n = i
        return (m1 + m2) if m2n not in e[m1n] else (m1 + m2 - 1)
            
        
        