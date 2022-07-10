class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        self.mem = dict()
        self.mem[len(cost) - 1] = cost[-1]
        self.rec(0, cost)
        return min(self.mem[0], self.mem[1])
        
    def rec(self, pos, cost):
        if pos in self.mem:
            return self.mem[pos]
        elif pos == len(cost) - 2:
            self.mem[pos] = cost[pos] + self.rec(pos+1, cost)
            return self.mem[pos]
        else:
            self.mem[pos] = cost[pos] + min(self.rec(pos+1, cost), self.rec(pos+2, cost))
            return self.mem[pos]