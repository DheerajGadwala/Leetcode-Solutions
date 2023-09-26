class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Monotonic Stack
        last = dict()
        for i in range(len(s)):
            last[s[i]] = i
        stk = []
        added = set()
        for i in range(len(s)):
            while len(stk) > 0 and stk[-1] > s[i] and last[stk[-1]] > i and s[i] not in added:
                added.remove(stk.pop())
            if s[i] not in added:
                stk.append(s[i])
                added.add(s[i])
        return ''.join(stk)