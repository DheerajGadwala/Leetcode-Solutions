class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        
        @cache
        def res(word, i=0):
            if i == len(word):
                return True
            n = len(word)
            ans = False
            for j in range(i, n+1):
                x = word[i:j]
                ans |= x in s and res(word, j) and not (j == n and i == 0)
            return ans
        
        ret = []
        for word in words:
            if res(word):
                ret.append(word)
        
        return ret
                