class Trie:

    def __init__(self):
        self.head = [dict(), 0]

    def insert(self, word: str) -> None:
        curr = self.head
        for i in word:
            if i not in curr[0]:
                curr[0][i] = [dict(), 0]
            curr = curr[0][i]
        curr[1] += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.head
        for i in word:
            if i not in curr[0]:
                return 0
            else:
                curr = curr[0][i]
        return curr[1]

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.head
        ret = 0
        for i in prefix:
            if i not in curr[0]:
                return 0
            else:
                curr = curr[0][i]
        q = [curr]
        while len(q) != 0:
            u = q.pop(0)
            ret += u[1]
            for v in u[0]:
                q.append(u[0][v])
        return ret

    def erase(self, word: str) -> None:
        curr = self.head
        for i in word:
            if i not in curr[0]:
                return
            else:
                curr = curr[0][i]
        curr[1] -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)