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
        l = l[::-1] if not d else l
        return ''.join(l)