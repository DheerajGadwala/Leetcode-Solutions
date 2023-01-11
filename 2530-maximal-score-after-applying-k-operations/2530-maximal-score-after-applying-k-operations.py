class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        q = [-i for i in nums]
        heapify(q)
        ans = 0
        while k > 0:
            n = -heappop(q)
            ans += n
            heappush(q, -math.ceil(n/3))
            k -= 1
        return ans