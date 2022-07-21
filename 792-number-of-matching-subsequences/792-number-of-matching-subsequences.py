class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        visited = set()
        np = set()
        for word in words:
            if word in visited:
                cnt += 1
                continue
            if word in np:
                continue
            i, j = [0, 0]
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i+=1
                    j+=1
                    visited.add(word[:i])
                else:
                    j+=1
            if i == len(word):
                cnt+=1
            else:
                for t in range(i, len(word)):
                    np.add(word[:t+1])
        return cnt