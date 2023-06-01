class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        lists = [list() for i in range(k)]
        for num in nums:
            lists[num%k].append(num)
        ans = 1
        
        for l in lists:
            m = len(l)
            @cache
            def res(pos = 0):
                if pos == m:
                    return 1
                elif pos == m - 1:
                    return 2
                elif l[pos] + k == l[pos + 1]:
                    return res(pos + 1) + res(pos + 2)
                else:
                    return res(pos + 1) * 2
            ans *= res()
        
        return ans
            