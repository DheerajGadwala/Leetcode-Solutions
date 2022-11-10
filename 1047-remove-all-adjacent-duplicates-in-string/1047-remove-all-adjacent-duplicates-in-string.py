class Solution:
    def removeDuplicates(self, s: str) -> str:
        x = []
        for i in s:
            if len(x) > 0 and x[-1] == i:
                x.pop()
            else:
                x.append(i)
        return ''.join(x)
        