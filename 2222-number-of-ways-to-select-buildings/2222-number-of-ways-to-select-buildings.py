class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        zeroCount = 0
        for i in s:
            if i == '0':
                zeroCount += 1
        oneCount = n - zeroCount
        runningZeroes = 0
        ans = 0
        for i in range(n):
            leftZeroes = runningZeroes
            leftOnes = i - leftZeroes
            rightZeroes = zeroCount - leftZeroes - (1 if s[i] == '0' else 0)
            rightOnes = oneCount - leftOnes - (1 if s[i] == '1' else 0)
            if s[i] == '0':
                ans += leftOnes * rightOnes
                runningZeroes += 1
            else:
                ans += leftZeroes * rightZeroes
        return ans
        
        