class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mem = dict()
        MOD = 10**9 + 7
        arr.sort()
        n = len(arr)
        ans = 0
        for i in range(n):
            total = 1
            for j in range(i + 1):
                if arr[i] / arr[j] in mem:
                    total += mem[arr[j]] * mem[arr[i] / arr[j]]
                    total %= MOD
            mem[arr[i]] = total
            ans += total
            ans %= MOD
        return ans