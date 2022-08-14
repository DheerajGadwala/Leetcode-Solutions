class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordList = set(wordList)
        
        def canBeNext(c, n):
            diffCount = 0
            for i in range(len(c)):
                if c[i] != n[i]:
                    diffCount += 1
            return diffCount == 1
        
        q = [beginWord]
        dep = {beginWord: 0}
        
        while len(q) != 0:
            u = q.pop(0)
            if u == endWord:
                break
            for i in range(len(u)):
                for j in 'qwertyuiopasdfghjklzxcvbnm':
                    v = u[:i] + j + u[i+1:]
                    if v in wordList and v not in dep:
                        dep[v] = dep[u] + 1
                        q.append(v)

        d = 0 if endWord not in dep else dep[endWord]

        if d == 0:
            return []
        
        visited = set()
        
        @cache
        def dfs(u = beginWord, dep = d):
            if dep == 0 and u == endWord:
                return [[u]]
            elif dep > 0:
                ret = []
                for i in range(len(u)):
                    for j in 'qwertyuiopasdfghjklzxcvbnm':
                        v = u[:i] + j + u[i+1:]
                        if v in wordList:
                            ret += dfs(v, dep - 1)
                ret = [[u] + k for k in ret]
                return ret
            else:
                return []
        
        return dfs()
                    