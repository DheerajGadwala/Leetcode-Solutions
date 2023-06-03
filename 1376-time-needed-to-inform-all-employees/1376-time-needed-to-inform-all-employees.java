class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        List<Integer>[] adj = new List[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            if (i != headID)
                adj[manager[i]].add(i);
        }
        Queue<Integer> q = new LinkedList<>();
        int[] time = new int[n];
        q.add(headID);
        time[headID] = informTime[headID];
        int ans = informTime[headID];
        while (q.size() != 0) {
            int u = q.poll();
            for (int v: adj[u]) {
                q.add(v);
                time[v] = informTime[v] + time[u];
                ans = Math.max(ans, time[v]);
            }
        }
        return ans;
    }
}