class Solution {
    
    Set<Integer>[] adj;
    boolean[] visited;
    
    public int maximumDetonation(int[][] bombs) {
        
        // 1. Create adjacency list 
        // 2. Perform DFS.
        // # Note: Return largest component's size.
        
        // 1. Create Adjacency List
        int n = bombs.length;
        Set<Integer>[] adj = new HashSet[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new HashSet<>();
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    int x1 = bombs[i][0], x2 = bombs[j][0];
                    int y1 = bombs[i][1], y2 = bombs[j][1];
                    long r = bombs[i][2];
                    if (Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2) <= r * r) {
                        adj[i].add(j);
                    }
                }
            }
        }
        
        // 2. Perform DFS to get max component size, O(len(bombs)^3) | O(n^3)
        this.adj = adj;
        int ans = 1;
        for (int i = 0; i < n; i++) {
            this.visited = new boolean[n];
            ans = Math.max(ans, dfs(i));
        }
        return ans;
    }
    
    public int dfs(int u) {
        visited[u] = true;
        int ret = 1;
        for (int v: adj[u]) {
            if (!visited[v]) {
                ret += dfs(v);
            }
        }
        return ret;
    }
}