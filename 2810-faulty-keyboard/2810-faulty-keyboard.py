class Solution:
    def finalString(self, s: str) -> str:
        d = True
        l = deque([])
        for i in s:
            if i == 'i':
                d = not d
            elif d:
                l.append(i)
            else:
                l.appendleft(i)
        l = list(l)
        return ''.join(l) if d else ''.join(l[::-1])