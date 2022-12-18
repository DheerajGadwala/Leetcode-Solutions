class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        s = []
        ret = [0] * n
        for i in range(n):
            while len(s) > 0 and t[s[-1]] < t[i]:
                ret[s.pop()] = i - s[-1]
            s.append(i)
        return ret