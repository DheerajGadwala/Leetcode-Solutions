class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif s == goal:
            return len(set(s)) != len(s)
        else:
            uneq = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    uneq.append(i)
            if len(uneq) != 2:
                return False
            else:
                return s[uneq[0]] == goal[uneq[1]] and s[uneq[1]] == goal[uneq[0]]