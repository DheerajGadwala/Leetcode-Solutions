class Solution:
    def frequencySort(self, s: str) -> str:
        x = Counter(s)
        s = list(s)
        s.sort(key = lambda y: (-x[y], y))
        return ''.join(s)