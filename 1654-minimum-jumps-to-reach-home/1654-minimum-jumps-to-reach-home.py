class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q=[[0,False,0]]
        seen=set()
        while q:
            num,isBack,ct=q.pop(0)
            if num==x:
                return ct
            if num+a < 6000 and num+a not in forbidden and (num+a, False) not in seen:
                seen.add((num+a, False))
                q.append([num+a,False,ct+1])
            if num-b>=0 and num-b not in forbidden and not isBack and (num-b, True) not in seen:
                seen.add((num-b, True))
                q.append([num-b,True,ct+1])

        return -1