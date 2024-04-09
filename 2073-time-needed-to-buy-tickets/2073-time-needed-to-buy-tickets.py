class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        ans = 0
        while tickets[k] != 0:
            mn = math.inf
            for i in range(n):
                if tickets[i] != 0:
                    mn = min(mn, tickets[i])
            for i in range(n):
                if tickets[i] != 0:
                    tickets[i] -= mn
                    ans += mn
                if i == k and tickets[i] == 0:
                    mn -= 1
        return ans