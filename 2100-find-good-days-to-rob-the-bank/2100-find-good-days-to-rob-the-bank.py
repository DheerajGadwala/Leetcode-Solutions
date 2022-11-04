class Solution:
    def goodDaysToRobBank(self, l: List[int], t: int) -> List[int]:
        n = len(l)
        if n < 2*t+1:
            return []
        dec, inc = 0, 0
        for i in range(1, t + 1):
            if l[i] <= l[i-1]:
                dec += 1
        for i in range(t+1, 2*t+1):
            if l[i] >= l[i-1]:
                inc += 1
        ret = []
        if dec == t and inc == t:
            ret.append(t)
        for i in range(t+1, n-t):
            if l[i-t] <= l[i-t-1]:
                dec -= 1
            if l[i] <= l[i-1]:
                dec += 1
            if l[i-1] <= l[i]:
                inc -= 1
            if l[i+t-1] <= l[i+t]:
                inc += 1
            if inc == t and dec == t:
                ret.append(i)
        return ret