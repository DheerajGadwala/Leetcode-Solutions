import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        q = [(nums1[0] + nums2[0], 0, 0)]
        
        ans = []
        
        visited = {(0, 0), }
        
        while len(q) != 0 and len(ans) < k:
            
            u = heapq.heappop(q)
            
            ans.append((nums1[u[1]], nums2[u[2]]))
            
            if u[1] + 1 < len(nums1) and (u[1] + 1, u[2]) not in visited:
                
                heapq.heappush(q, (nums1[u[1] + 1] + nums2[u[2]], u[1] + 1, u[2]))
                visited.add((u[1] + 1, u[2]))
            
            if u[2] + 1 < len(nums2) and (u[1], u[2] + 1) not in visited:
                
                heapq.heappush(q, (nums1[u[1]] + nums2[u[2] + 1], u[1], u[2] + 1))
                visited.add((u[1], u[2] + 1))
        
        return ans
            
            
            
            