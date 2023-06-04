class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        boolean[] visited = new boolean[n];
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                Queue<Integer> q = new LinkedList<>();
                q.add(i);
                while (q.size() != 0) {
                    int u = q.poll();
                    for (int j = 0; j < n; j++) {
                        if (!visited[j] && isConnected[u][j] == 1) {
                            visited[j] = true;
                            q.add(j);
                        }
                    }
                }
                ans++;
            }
        }
        return ans;
    }
}