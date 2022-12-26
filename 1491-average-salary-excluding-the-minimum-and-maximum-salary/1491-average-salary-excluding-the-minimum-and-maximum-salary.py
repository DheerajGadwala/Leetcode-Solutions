class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        s = 0
        mx = -math.inf
        mn = math.inf
        for i in salary:
            s += i
            mx = max(mx, i)
            mn = min(mn, i)
        return (s - mx - mn) / (n - 2)