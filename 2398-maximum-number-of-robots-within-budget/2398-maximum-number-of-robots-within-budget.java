class Solution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        
        // monotonically decreasing queue
        Deque<Integer> q = new LinkedList<>();
        // window first and last pointers
        int n = chargeTimes.length, f = 0, l = 0, ans = 0;
        // window sum
        long currSum = 0;
        
        while (f < n) {
            // maintain the monotonically decreasing property of the queue
            while (q.size() > 0 && chargeTimes[q.peekLast()] < chargeTimes[f]) q.pollLast();
            q.addLast(f);
            currSum += runningCosts[f++];
            // adjust l pointer for the current f pointer
            while (f!=l && chargeTimes[q.peekFirst()]+(f-l)*currSum > budget) {
                if (q.peekFirst() == l) q.pollFirst();
                currSum -= runningCosts[l++];
            }
            ans = Math.max(ans, f-l);
        }
        
        return ans;
    }
}