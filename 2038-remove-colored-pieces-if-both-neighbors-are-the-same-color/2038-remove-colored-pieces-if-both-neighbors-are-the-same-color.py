class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a, b = 0, 0
        n = len(colors)
        for i in range(2, n):
            if colors[i] == colors[i-1] and colors[i] == colors[i-2]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
        return a > b
            