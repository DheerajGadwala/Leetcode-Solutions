class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans=[] 
        people.sort(key=lambda x: (-x[0], x[1]))                
        for a in people:
            ans.insert(a[1], a)
        return ans