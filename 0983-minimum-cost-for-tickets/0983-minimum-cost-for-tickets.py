class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = [False] * 365
        for i in days:
            d[i-1] = True
        mem = dict()
        def res(day = 1):
            while day < 366 and not d[day-1]:
                day += 1
            if day >= 366:
                return 0
            elif day in mem:
                return mem[day]
            else:
                mem[day] = min(costs[0] + res(day + 1), costs[1] + res(day + 7), costs[2] + res(day + 30))
                return mem[day]
        return res()