class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endPoint = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endPoint = True
    
    def searchEnd(self, s, i):
        curr = self.root
        j = i
        end = None
        while j < len(s) and s[j] in curr.children:
            curr = curr.children[s[j]]
            if curr.endPoint:
                end = j + 1
            j += 1
        return end

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.addWord(word)
        intervals = []
        n = len(s)
        for i in range(n):
            start, end = i, t.searchEnd(s, i)
            if end is not None:
                intervals.append([start, end])
        merged = []
        for st, e in intervals:
            if len(merged) == 0:
                merged.append([st, e])
            elif st <= merged[-1][1]:
                merged[-1][1] = max(e, merged[-1][1])
            else:
                merged.append([st, e])
                
        #print(intervals, merged)
        starts = {i[0] for i in merged}
        ends = {i[1] - 1 for i in merged}
        ret = []
        for i in range(n):
            if i in starts:
                ret.append('<b>')
            ret.append(s[i])
            if i in ends:
                ret.append('</b>')
        return ''.join(ret)
        