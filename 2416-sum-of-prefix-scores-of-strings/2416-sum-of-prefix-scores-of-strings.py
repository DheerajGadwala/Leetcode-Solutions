class Node:
    def __init__(self):
        self.children = [None] * 26
        self.cnt = 0
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Node()
        for word in words:
            curr = root
            for i in word:
                ind = ord(i) - ord('a')
                if curr.children[ind] is None:
                    curr.children[ind] = Node()
                curr = curr.children[ind]
                curr.cnt += 1
        
        ret = []
        for word in words:
            curr = root
            nxt = 0
            for i in word:
                ind = ord(i) - ord('a')
                if curr.children[ind] is not None:
                    curr = curr.children[ind]
                    nxt += curr.cnt
                else:
                    break
            ret.append(nxt)
        return ret