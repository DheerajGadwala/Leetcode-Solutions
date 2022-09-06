class Solution {
    public int findMaxValueOfEquation(int[][] points, int k) {
        
        Deque<Integer> q = new LinkedList<>();
        int f = 0, l = 0, n = points.length, ans = Integer.MIN_VALUE;
        while (f < n) {
            while (q.size() > 0 && points[f][0] - points[q.peekFirst()][0] > k) {
                q.pollFirst();
            }
            if (q.size() > 0)
                ans = Math.max(ans, points[f][1] + points[q.peekFirst()][1] - points[q.peekFirst()][0] + points[f][0]);
            while (q.size() > 0 && points[q.peekLast()][1] - points[q.peekLast()][0] < points[f][1] - points[f][0])
                q.pollLast();
            q.addLast(f);
            f++;
        }
        
        return ans;
    }
}