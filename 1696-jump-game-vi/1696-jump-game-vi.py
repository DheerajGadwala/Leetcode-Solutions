class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        ans = 0
        negs = []
        temp = [0]
        for i in range(len(nums)):
            if nums[i] >= 0 or i == 0 or i == len(nums) - 1:
                ans += nums[i]
                if len(temp) > k:
                    negs.append(temp)
                    temp = [0]
                else:
                    temp = [0]
            else:
                temp.append(nums[i])
        
        mem = dict()
        def res(pos = 0):
            if pos in mem:
                return mem[pos]
            elif pos > len(l):
                return -math.inf
            elif pos == len(l):
                return 0
            else:
                mxPos = None
                mx = -math.inf
                if pos + k >= len(l):
                    mem[pos] = l[pos]
                    return l[pos]
                for i in range(1, min(k+1, len(l) - pos + 1)):
                    if mx <= l[pos + i]:
                        mx = l[pos + i]
                        mxPos = i
                ret = -math.inf
                for i in range(mxPos, min(k+1, len(l) - pos + 1)):
                    ret = max(ret, res(pos+i))
                mem[pos] = ret + l[pos]
                return ret + l[pos]
        
        for l in negs:
            mem = dict()
            ans += res()
        
        return ans
                    