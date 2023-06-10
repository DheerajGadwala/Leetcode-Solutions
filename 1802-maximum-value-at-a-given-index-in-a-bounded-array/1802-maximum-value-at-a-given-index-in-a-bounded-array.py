class Solution:
    def maxValue(self, n, index, maxSum):
        maxSum -= n
        l, h = 0, maxSum
        while l < h:
            mid = (l + h + 1) // 2
            left_start = max(mid - index, 0)
            left = (mid + left_start) * (mid - left_start + 1) / 2
            right_start = max(mid - ((n - 1) - index), 0)
            right = (mid + right_start) * (mid - right_start + 1) / 2
            currSum = left + right - mid
            if currSum <= maxSum:
                l = mid
            else:
                h = mid - 1
        return l + 1