class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> nodes = new HashSet<>();
        for (int k: nums) {
            nodes.add(k);
        }
        Set<Integer> visited = new HashSet<>();
        int ans = 0;
        for (int k: nums) {
            ans = Math.max(ans, bfs(k, visited, nodes));
        }
        return ans;
    }
    
    private static int bfs(int s, Set<Integer> visited, Set<Integer> nodes) {
        int ans = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(s);
        visited.add(s);
        while (q.size() != 0) {
            int u = q.poll();
            ans++;
            if (nodes.contains(u+1) && !visited.contains(u+1)) {
                q.add(u+1);
                visited.add(u+1);
            }
            if (nodes.contains(u-1) && !visited.contains(u-1)) {
                q.add(u-1);
                visited.add(u-1);
            }
        }
        return ans;
    }
}