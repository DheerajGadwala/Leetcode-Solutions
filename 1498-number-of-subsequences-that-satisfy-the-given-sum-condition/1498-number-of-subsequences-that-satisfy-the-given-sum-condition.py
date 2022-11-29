class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        ans=0
        mod=pow(10,9)+7
        while i<=j:
            if nums[i]+nums[j]>target:
                j-=1
            else:
                ans+=pow(2,j-i,mod)
                i+=1
        return ans%mod