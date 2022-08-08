class Solution:
    def lengthOfLIS(self, l: List[int]) -> int:
        if(l==[]):
            return 0
        m = [l[0]]
        for i in range(1, len(l)):
            if(l[i]>m[-1]):
                m.append(l[i])
            else:
                low = 0
                high = len(m)-1
                while(low<=high):
                    mid = (low+high)//2
                    if(l[i]>m[mid]):
                        low=mid+1
                    elif(l[i]<m[mid]):
                        high=mid-1
                    else:
                        m[mid] = l[i]
                        break
                else:
                    m[low] = l[i]
        return len(m)