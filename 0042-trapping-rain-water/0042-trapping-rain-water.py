class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stk = []
        ans = 0
        for i in range(n):
            length = 0
            while len(stk) > 0 and height[stk[-1][0]] < height[i]:
                popped = stk.pop()
                hei = 0 if len(stk) == 0 else (min(height[stk[-1][0]], height[i]) - height[popped[0]])
                length += popped[1] + 1
                ans += hei * length
            stk.append((i, length))
        return ans