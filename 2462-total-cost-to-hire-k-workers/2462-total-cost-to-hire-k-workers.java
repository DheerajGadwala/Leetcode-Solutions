class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        int n = costs.length;
        PriorityQueue<Integer> q = new PriorityQueue<>((a, b) -> {
            int i = Integer.compare(costs[a], costs[b]);
            if (i == 0)
                return Integer.compare(a, b);
            else
                return i;
        });
        int i = 0, j = n - 1;
        while (i < candidates && i < n) {
            q.add(i++);
        }
        while (j > -1 && j > i && n - 1 - j < candidates) {
            q.add(j--);
        }
        long ans = 0;
        while (k-- > 0) {
            int polled = q.poll();
            ans += costs[polled];
            if (polled < i && i <= j)
                q.add(i++);
            else if (polled > j && i<= j)
                q.add(j--);
        }
        return ans;
    }
}