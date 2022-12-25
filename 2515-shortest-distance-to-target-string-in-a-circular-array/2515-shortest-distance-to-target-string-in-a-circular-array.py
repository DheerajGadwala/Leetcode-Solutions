class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        n = len(words)
        i = startIndex
        for j in range(n):
            f = (i + j) % n
            b = (i - j + n) % n
            if words[f] == target or words[b] == target:
                return j
        return -1
            