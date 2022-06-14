class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def res(i = 0, j = 0):
            if i == len(word1) and j == len(word2):
                return 0
            elif i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i
            elif word1[i] == word2[j]:
                return res(i+1, j+1)
            else:
                return 1 + min(res(i+1, j), res(i, j+1))
        return res()