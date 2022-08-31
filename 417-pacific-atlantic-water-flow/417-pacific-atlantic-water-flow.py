class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        
        neighbour = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        isValid = lambda x, y: x > -1 and y > -1 and x < len(grid) and y < len(grid[x])
        
        pacificV = set()
        pacificQ = []
        
        for i in range(len(grid)):
            pacificV.add((i, 0))
            pacificQ.append((i, 0))
        
        for i in range(len(grid[0])):
            pacificV.add((0, i))
            pacificQ.append((0, i))
        
        while len(pacificQ) != 0:
            u = pacificQ.pop(0)
            for vc in neighbour:
                v = (u[0] + vc[0], u[1] + vc[1])
                if isValid(*v) and v not in pacificV and grid[v[0]][v[1]] >= grid[u[0]][u[1]]:
                    pacificQ.append(v)
                    pacificV.add(v)

        atlanticV = set()
        atlanticQ = []
        
        for i in range(len(grid)):
            atlanticV.add((i, len(grid[i]) - 1))
            atlanticQ.append((i, len(grid[i]) - 1))
        
        for i in range(len(grid[0])):
            atlanticV.add((len(grid) - 1, i))
            atlanticQ.append((len(grid) - 1, i))
        
        while len(atlanticQ) != 0:
            u = atlanticQ.pop(0)
            for vc in neighbour:
                v = (u[0] + vc[0], u[1] + vc[1])
                if isValid(*v) and v not in atlanticV and grid[v[0]][v[1]] >= grid[u[0]][u[1]]:
                    atlanticQ.append(v)
                    atlanticV.add(v)
        
        return pacificV.intersection(atlanticV)
        
                    