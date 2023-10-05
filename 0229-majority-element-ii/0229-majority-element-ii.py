class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2, cnt1, cnt2 = 0, 0, 0, 0
        for i in nums:
            if c1 == i:
                cnt1+=1
            elif c2 == i:
                cnt2+=1
            elif cnt1 == 0:
                c1 = i
                cnt1 = 1
            elif cnt2 == 0:
                c2 = i
                cnt2 = 1
            else:
                cnt1-=1
                cnt2-=1
        ret = set()
        for i in [c1, c2]:
            cnt = 0
            for j in nums:
                if i == j:
                    cnt += 1
            if cnt > len(nums) // 3:
                ret.add(i)
        return ret
        
        
        