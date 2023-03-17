class Trie:

    def __init__(self):
        self.root = [dict(), False]

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr[0]:
                curr[0][c] = [dict(), False]
            curr = curr[0][c]
        curr[1] = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr[0]:
                return False
            curr = curr[0][c]
        return curr[1]

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr[0]:
                return False
            curr = curr[0][c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)