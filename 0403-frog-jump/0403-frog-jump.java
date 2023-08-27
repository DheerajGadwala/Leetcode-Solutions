class Solution {
    public boolean canCross(int[] stones) {
        Map<Integer, Integer> stonePosition = new HashMap<>();
        int n = stones.length;
        for (int i = 0; i < n; i++) {
            stonePosition.put(stones[i], i);
        }
        Queue<Integer[]> q = new LinkedList<>();
        Set<Integer> visited = new HashSet<>(); 
        q.add(new Integer[] {0, 1});
        visited.add(0*n+1);
        while (q.size() != 0) {
            Integer[] uk = q.poll();
            int u = uk[0], k = uk[1];
            int curr = stones[u];
            int next = curr + k;
            int v = stonePosition.getOrDefault(next, -1);
            if (v == n-1) return true;
            if (v != -1) {
                if (k-1 > 0 && !visited.contains(n*v+k-1)) {
                    q.add(new Integer[] {v, k-1});
                    visited.add(n*v+k-1);
                }
                if (!visited.contains(n*v+k)) {
                    q.add(new Integer[] {v, k});
                    visited.add(n*v+k);
                }
                if (!visited.contains(n*v+k+1)) {
                    q.add(new Integer[] {v, k+1});
                    visited.add(n*v+k+1);
                }
                
            }
        }
        return false;
    }
}