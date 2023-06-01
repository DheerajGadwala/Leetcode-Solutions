class Solution {
    
    private boolean isValid(int i, int j, int[][] grid) {
        return i < grid.length && i > -1 && j < grid[i].length && j > -1 && grid[i][j] == 0;
    }
    
    public int shortestPathBinaryMatrix(int[][] grid) {
        
        int k = grid.length;
        
        int[][] neighbours = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}};
        
        Map<Integer, Integer> mp = new HashMap<>();
        
        Queue<Integer[]> q = new LinkedList<>();
        
        if (grid[0][0] == 0) {
            grid[0][0] = 1;
            q.add(new Integer[] {0, 0});
            mp.put(0, 1);
        }
        
        while (q.size() != 0) {
            
            Integer[] u = q.poll();
            
            // System.out.println(u[0] + " " + u[1] + " " + u[0] + " " + (u[0] * k + u[1]));
            
            if (u[0] * k + u[1] == (k - 1) * k + k - 1) {
                return mp.get((k-1)*k+k-1);
            }
            
            for (int[] n: neighbours) {
                
                Integer[] v = {u[0] + n[0], u[1] + n[1]};
                
                if (isValid(v[0], v[1], grid)) {
                    
                    grid[v[0]][v[1]] = 1;
                    
                    q.add(v);
                    
                    mp.put(v[0] * k + v[1], mp.get(u[0] * k + u[1]) + 1);
                }
            }
        }
        
        return -1;
        
    }
}