class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = dict()
        for i in range(len(keyboard)):
            pos[keyboard[i]] = i
        curr = 0
        ans = 0
        for w in word:
            ans += abs(curr - pos[w])
            curr = pos[w]
        return ans