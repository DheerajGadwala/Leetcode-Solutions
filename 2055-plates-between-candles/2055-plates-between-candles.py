class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        mp = dict()
        lkupl = []
        lkupr = []
        plates = []
        for i in range(n):
            if s[i] == '|':
                plates.append(i)
                lkupl.append(len(plates) - 1)
                lkupr.append(len(plates) - 1)
            else:
                lkupl.append(len(plates))
                lkupr.append(len(plates) - 1)
        ans = []
        for l, r in queries:
            pl, pr = lkupl[l], lkupr[r]
            if pl == len(plates) or pr == -1 or pr <= pl:
                ans.append(0)
            else:
                ans.append(plates[pr] - plates[pl] - 1 - (pr - pl - 1))
        return ans