class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans=0
        if n==0:
            return 1
        def solve(i,has):
            nonlocal ans
            # print(has,i,n)
            if i>n:
                return
            ans+=1
            for num in range(1 if i == 0 else 0, 10):
                if num not in has:
                    has.add(num)
                    solve(i+1,has)
                    has.remove(num)
        solve(0,set())
        
        return ans