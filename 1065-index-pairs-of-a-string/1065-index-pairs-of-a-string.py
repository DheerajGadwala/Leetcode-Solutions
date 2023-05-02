class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        head = [dict(), False]
        for word in words:
            curr = head
            for c in word:
                if c not in curr[0]:
                    curr[0][c] = [dict(), False]
                curr = curr[0][c]
            curr[1] = True
        n = len(text)
        ret = []
        for i in range(n):
            curr = head
            for j in range(i, n):
                c = text[j]
                if c not in curr[0]:
                    break
                else:
                    curr = curr[0][c]
                if curr[1]:
                    ret.append([i, j])
        return ret