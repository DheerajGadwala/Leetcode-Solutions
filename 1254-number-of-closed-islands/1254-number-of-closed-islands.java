class Solution {
    public int closedIsland(int[][] grid) {
        if(grid == null || grid.length == 0) return 0;
        int count = 0;
        
        for (int i = 0; i < grid.length; i++) {
            dfs(grid, i, 0);
            dfs(grid, i, grid[0].length - 1);
        }
        for (int i = 0; i < grid[0].length; i++) {
            dfs(grid, 0, i);
            dfs(grid, grid.length - 1, i);
        }
        
        for(int i =0;i<grid.length;i++)
        {
            for(int j = 0;j<grid[0].length;j++)
            {
                if(grid[i][j] == 0)
                {
                    dfs(grid,i,j);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    private void dfs(int[][] grid, int row, int col)
    {
        //base
        if(row==grid.length || col == grid[0].length || row<0 || col<0 || grid[row][col]!=0) return;
            
        //logic
        grid[row][col] = 1;
        dfs(grid,row-1,col);
        dfs(grid,row+1,col);
        dfs(grid,row,col-1);
        dfs(grid,row,col+1);
        
    }
}