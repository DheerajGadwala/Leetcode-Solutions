class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        
        m, n = len(mat), len(mat[0])
        visited = set()
        ans = 0
        
        def res(pos = 0):
            nonlocal ans
            if len(visited) == cols or pos == n:
                cnt = 0
                for row in mat:
                    included = True
                    for i in range(len(row)):
                        if row[i] == 1 and i not in visited:
                            included = False
                    if included:
                        cnt += 1
                ans = max(ans, cnt)
            else:
                visited.add(pos)
                res(pos + 1)
                visited.remove(pos)
                res(pos + 1)
        res()
        return ans
            