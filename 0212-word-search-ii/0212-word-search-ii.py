class TrieNode:
    def __init__(self):
        self.child = dict()
        self.endPoint = False
    
    def add(self, w):
        curr = self
        for i in w:
            if i not in curr.child:
                curr.child[i] = TrieNode()
            curr = curr.child[i]
        curr.endPoint = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        head = TrieNode()
        for word in words:
            head.add(word)
        
        m, n = len(board), len(board[0])
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ret = set()
        visited = set()
        path = []
        
        def res(i=0, j=0, curr=head):
            nonlocal m, n
            c = board[i][j]
            visited.add((i, j))
            path.append(c)
            if c in curr.child:
                nxt = curr.child[c]
                if nxt.endPoint:
                    found = ''.join(path)
                    ret.add(found)
                    nxt.endPoint = False
                for nei in neighbours:
                    vi, vj = i + nei[0], j + nei[1]
                    if vi > -1 and vj > -1 and vi < m and vj < n and (vi, vj) not in visited:
                        res(vi, vj, nxt)
                if len(nxt.child) == 0:
                    del curr.child[c]
            path.pop()
            visited.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                res(i, j)
        
        return ret
                
        
                        
                    
                