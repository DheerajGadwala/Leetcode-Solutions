class Solution {
    public int hardestWorker(int n, int[][] logs) {
        int t = 0;
        int curr = 0;
        int id = 0;
        for (int[] log: logs) {
            if (log[1] - t > curr) {
                curr = log[1] - t;
                id = log[0];
            } 
            else if (log[1] - t == curr) {
                id = Math.min(id, log[0]);
            }
            t = log[1];
        }
        return id;
    }
}